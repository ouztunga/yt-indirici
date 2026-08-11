import os
import sys
import io
import tempfile

# PyInstaller --noconsole modunda stdout/stderr None olacağı için donduran hataları önle
if getattr(sys, 'frozen', False):
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

# PYWEBVIEW_GUI, import webview'den ÖNCE ayarlanmalıdır!
os.environ['PYWEBVIEW_GUI'] = 'edgechromium'
os.environ['WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS'] = '--disable-gpu-shader-disk-cache --disable-features=RendererCodeIntegrity'

import webview
import threading
import logging
import traceback
import base64
import json
from concurrent.futures import ThreadPoolExecutor

__version__ = "1.3.0"


def resource_path(relative_path):
    """PyInstaller ile paketlenmişse _MEIPASS, değilse dosya dizini."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)


logging.basicConfig(
    filename='indirici_hata.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# pywebview'in iç hatalarını (özellikle EdgeChromium accessibility bug) loglamasını engelle
logging.getLogger('pywebview').setLevel(logging.CRITICAL)


class EliteApi:
    """pywebview JS API — tüm backend mantığı burada."""

    def __init__(self):
        import time
        self.base_path = os.path.dirname(os.path.realpath(
            sys.executable if getattr(sys, 'frozen', False) else __file__
        ))
        self.download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        self.window = None          # pywebview pencere referansı
        self.is_ready = False       # WebView2 tam yüklendi flag'i
        self.last_info = None       # Son analiz edilen video bilgisi
        self.should_stop = False    # İndirme durdurma flag'i
        self.pause_event = threading.Event()
        self.pause_event.set()      # Başlangıçta duraklatılmamış
        self._js_lock = threading.Lock()  # evaluate_js deadlock kilidi
        self._last_progress_time = 0      # UI throttling zaman damgası
        self.last_downloaded_path = None  # En son indirilen (playlist alt klasörü dahil) yol
        self._current_analyze_id = 0      # İptal kontrolü için analiz ID'si

    # ═══════════════════════════════════════════════════════════
    #  YARDIMCI METOTLAR
    # ═══════════════════════════════════════════════════════════

    def _js(self, code):
        """Thread-safe evaluate_js wrapper (Deadlock korumalı, timeout'lu ve ready-checked)."""
        if not self.window or not getattr(self, 'is_ready', False):
            return
        try:
            if self._js_lock.acquire(timeout=0.2):
                try:
                    self.window.evaluate_js(code)
                finally:
                    self._js_lock.release()
        except Exception:
            pass

    def _find_cookie_source(self):
        """Öncelikle local cookies.txt var mı bak, yoksa tarayıcı çerezlerini tara."""
        # 1. cookies.txt kontrolü (En kararlı yöntem)
        possible_txts = [
            os.path.join(self.base_path, 'cookies.txt'),
            os.path.join(os.getcwd(), 'cookies.txt'),
            os.path.join(os.path.expanduser("~"), "Downloads", "cookies.txt"),
            os.path.join(os.path.expanduser("~"), "Desktop", "cookies.txt"),
        ]
        for txt in possible_txts:
            if os.path.exists(txt) and os.path.getsize(txt) > 0:
                return ('file', txt)

        # 2. Mevcut tarayıcı çerezleri
        local = os.environ.get('LOCALAPPDATA', '')
        appdata = os.environ.get('APPDATA', '')

        browsers = [
            ('firefox', os.path.join(appdata, r'Mozilla\Firefox\Profiles')),
            ('edge', os.path.join(local, r'Microsoft\Edge\User Data\Default\Network\Cookies')),
            ('chrome', os.path.join(local, r'Google\Chrome\User Data\Default\Network\Cookies')),
            ('brave', os.path.join(local, r'BraveSoftware\Brave-Browser\User Data\Default\Network\Cookies')),
            ('opera', os.path.join(appdata, r'Opera Software\Opera Stable\Network\Cookies')),
            ('vivaldi', os.path.join(local, r'Vivaldi\User Data\Default\Network\Cookies')),
        ]

        for name, cookie_path in browsers:
            if os.path.exists(cookie_path):
                return ('browser', name)

        return (None, None)

    def _ydl_opts(self, url="", force_browser=None, force_no_cookies=False, **extra):
        """Tüm yt-dlp çağrıları için ortak ve optimize edilmiş ayarlar."""
        opts = {
            'quiet': True,
            'no_warnings': True,
            'check_formats': False,
            'nocheckcertificate': True,
            'socket_timeout': 10,
            'concurrent_fragment_downloads': 4,
            'http_chunk_size': 10485760,  # 10MB chunk
            'buffersize': 1024 * 1024,   # 1MB buffer
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            },
        }

        if not force_no_cookies:
            if force_browser:
                opts['cookiesfrombrowser'] = (force_browser, None, None, None)
            else:
                source_type, source_val = self._find_cookie_source()
                if source_type == 'file':
                    opts['cookiefile'] = source_val
                elif source_type == 'browser' and url and any(d in url.lower() for d in ['instagram.com', 'tiktok.com', 'twitter.com', 'x.com']):
                    opts['cookiesfrombrowser'] = (source_val, None, None, None)

        opts.update(extra)
        return opts

    # ═══════════════════════════════════════════════════════════
    #  BOYUT HESAPLAMA
    # ═══════════════════════════════════════════════════════════

    def _calc_size(self, info_dict, quality):
        """Tek bir kalite için MB cinsinden boyut hesapla.

        yt-dlp format listesi kaliteye göre artan sıralıdır (son = en iyi).
        bestvideo/bestaudio = listenin sonundaki eleman.
        """
        try:
            duration = info_dict.get('duration')
            formats = info_dict.get('formats', [])

            # ── MP3 ───────────────────────────────────────────
            if quality == "audio":
                # FFmpeg → MP3 192 kbps dönüşümü
                if duration and duration > 0:
                    size_bytes = duration * 192000 / 8 * 1.03   # +%3 container overhead
                    return round(size_bytes / (1024 * 1024), 1)
                return None

            # ── Video ─────────────────────────────────────────
            if not formats:
                return None

            target_h = int(quality)

            # Video-only formatlar (yt-dlp bestvideo mantığı)
            video_fmts = [
                f for f in formats
                if f.get('vcodec') not in (None, 'none')
                and f.get('acodec') in (None, 'none')
                and 0 < (f.get('height') or 0) <= target_h
            ]

            # Audio-only formatlar (yt-dlp bestaudio mantığı)
            audio_fmts = [
                f for f in formats
                if f.get('vcodec') in (None, 'none')
                and f.get('acodec') not in (None, 'none')
            ]

            if video_fmts:
                best_v = video_fmts[-1]     # Son = en iyi (yt-dlp sıralaması)
                best_a = audio_fmts[-1] if audio_fmts else None

                v_size = best_v.get('filesize') or best_v.get('filesize_approx')
                a_size = 0
                if best_a:
                    a_size = best_a.get('filesize') or best_a.get('filesize_approx') or 0

                # 1) filesize varsa doğrudan kullan
                if v_size:
                    return round((v_size + a_size) / (1024 * 1024), 1)

                # 2) filesize yoksa bitrate × duration ile hesapla
                if duration and duration > 0:
                    v_kbps = best_v.get('tbr') or best_v.get('vbr') or 0
                    a_kbps = (best_a.get('abr') or best_a.get('tbr') or 128) if best_a else 128
                    if v_kbps > 0:
                        total_bytes = duration * (v_kbps + a_kbps) * 1000 / 8
                        return round(total_bytes / (1024 * 1024), 1)

            # Muxed formatlar (video+audio birlikte, genelde 720p altı)
            muxed = [
                f for f in formats
                if f.get('vcodec') not in (None, 'none')
                and f.get('acodec') not in (None, 'none')
                and 0 < (f.get('height') or 0) <= target_h
            ]
            if muxed:
                best_m = muxed[-1]
                fs = best_m.get('filesize') or best_m.get('filesize_approx')
                if fs:
                    return round(fs / (1024 * 1024), 1)
                if duration and duration > 0 and best_m.get('tbr'):
                    return round(duration * best_m['tbr'] * 1000 / 8 / (1024 * 1024), 1)

            # Son çare: tahmini bitrate tablosu
            if duration and duration > 0:
                fallback = {
                    "360": 500, "480": 800, "720": 1800, "1080": 3500,
                    "1440": 7000, "2160": 15000, "4320": 30000,
                }
                kbps = fallback.get(quality, 3500)
                return round(duration * kbps * 1000 / 8 / (1024 * 1024), 1)

        except Exception:
            pass
        return None

    def _calc_all_sizes(self, info_dict):
        """Tüm kaliteler için boyut hesapla → dict."""
        sizes = {}
        for q in ("audio", "360", "480", "720", "1080", "1440", "2160", "4320"):
            val = self._calc_size(info_dict, q)
            sizes[q] = f"{val} MB" if val else "Bilinmiyor"
        return sizes

    # ═══════════════════════════════════════════════════════════
    #  API: ANALİZ
    # ═══════════════════════════════════════════════════════════

    def analyze(self, url, quality="1080"):
        """JS'den çağrılır — arka plan thread'inde analiz başlatır."""
        if not url or url.strip() == "":
            self.last_info = None
            return
        self._current_analyze_id += 1
        current_id = self._current_analyze_id
        threading.Thread(target=self._analyze_thread, args=(url, current_id), daemon=True).start()

    def _analyze_thread(self, url, analyze_id):
        needs_cookies = any(d in url.lower() for d in ['instagram.com', 'tiktok.com', 'twitter.com', 'x.com'])
        is_playlist = 'list=' in url

        # Olası çerez seçeneklerini oluştur
        attempts = []
        source_type, source_val = self._find_cookie_source()
        if source_type == 'file':
            attempts.append({'type': 'file', 'val': source_val})
        elif source_type == 'browser' and needs_cookies:
            attempts.append({'type': 'browser', 'val': source_val})

        attempts.append({'type': 'none', 'val': None})

        last_error = None
        for attempt in attempts:
            if analyze_id != self._current_analyze_id:
                return  # Eski analiz iptal edildi

            try:
                if attempt['type'] == 'file':
                    ydl_opts = self._ydl_opts(url=url, noplaylist=not is_playlist, extract_flat='in_playlist' if is_playlist else False, lazy_playlist=True)
                elif attempt['type'] == 'browser':
                    ydl_opts = self._ydl_opts(url=url, force_browser=attempt['val'], noplaylist=not is_playlist, extract_flat='in_playlist' if is_playlist else False, lazy_playlist=True)
                else:
                    ydl_opts = self._ydl_opts(url=url, force_no_cookies=True, noplaylist=not is_playlist, extract_flat='in_playlist' if is_playlist else False, lazy_playlist=True)

                import yt_dlp
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if analyze_id != self._current_analyze_id:
                        return
                    self.last_info = info

                # Başarılı — sonucu işle
                title = self.last_info.get('title', 'Bilinmeyen Video')

                # Thumbnail bulma
                thumb = self.last_info.get('thumbnail', '')
                if not thumb and is_playlist:
                    entries = self.last_info.get('entries', [])
                    if entries and entries[0]:
                        thumb = entries[0].get('thumbnail', '')

                # Playlist / tekil video ayrımı
                playlist_entries = []
                max_height = 1080
                all_sizes = {}

                if is_playlist:
                    raw = self.last_info.get('entries', [])
                    for entry in raw:
                        if not entry:
                            continue
                        playlist_entries.append({
                            'id': entry.get('id'),
                            'title': entry.get('title', 'Bilinmeyen Video'),
                            'duration': entry.get('duration'),
                            'url': entry.get('url'),
                            'webpage_url': entry.get('webpage_url'),
                            'thumbnail': entry.get('thumbnail'),
                        })

                    self.all_sizes_cache = {}  # video_url -> {quality: size_str}
                    self.last_downloaded_path = None
                    count = len(playlist_entries)
                    all_sizes = {"audio": f"Playlist: {count} Ses"}
                    for q in ("360", "480", "720", "1080", "1440", "2160", "4320"):
                        all_sizes[q] = f"Playlist: {count} Video"

                else:
                    formats = self.last_info.get('formats', [])
                    heights = [f.get('height') for f in formats if f.get('height')]
                    if heights:
                        max_height = max(heights)
                    all_sizes = self._calc_all_sizes(self.last_info)

                if analyze_id != self._current_analyze_id:
                    return

                # Frontend'e gönder
                self._js(
                    f"updateUI({json.dumps(title)}, {json.dumps(thumb)}, "
                    f"{json.dumps(all_sizes)}, {json.dumps(url)}, "
                    f"{json.dumps(playlist_entries)}, {max_height})"
                )
                self._js(f"updateProgress(0, {json.dumps('✅ Video analiz edildi. İndirmeye hazır.')})")

                # Playlist ise arka planda detay çek
                if is_playlist and playlist_entries:
                    threading.Thread(
                        target=self._bg_playlist_details,
                        args=(playlist_entries,),
                        daemon=True,
                    ).start()

                return  # Başarılı — çık

            except Exception as e:
                last_error = e
                logging.error(f"Analiz denemesi ({attempt}) başarısız: {e}")
                # Sonraki denemeye geç
                continue

        if analyze_id != self._current_analyze_id:
            return

        # Tüm denemeler başarısız
        err_msg = str(last_error) if last_error else ""
        if needs_cookies and ("empty media" in err_msg or "login" in err_msg.lower() or "DPAPI" in err_msg or "Cookie" in err_msg):
            msg = "❌ Instagram videosu indirilemedi. Çözüm: Uygulama klasörüne 'cookies.txt' dosyası ekleyin veya açık tarayıcıları kapatın."
        else:
            msg = "❌ Hata: Video bulunamadı veya link geçersiz!"
        self._js(f"updateProgress(0, {json.dumps(msg)})")

    # ─── Playlist arka plan detayları ─────────────────────────

    def _bg_playlist_details(self, entries):
        """Her playlist videosunun boyut bilgilerini arka planda hesapla."""

        def fetch_one(idx, entry):
            if self.should_stop or not self.window:
                return
            video_id = entry.get('id')
            if not video_id:
                return

            qualities = ("audio", "360", "480", "720", "1080", "1440", "2160", "4320")

            try:
                video_url = entry.get('url') or entry.get('webpage_url') or f"https://www.youtube.com/watch?v={video_id}"
                import yt_dlp
                with yt_dlp.YoutubeDL(self._ydl_opts(url=video_url)) as ydl:
                    info = ydl.extract_info(video_url, download=False)
                    if info:
                        sizes = self._calc_all_sizes(info)
                        self._js(f"updatePlaylistItemSize({idx}, {json.dumps(sizes)})")
                        return
            except Exception as e:
                logging.error(f"Playlist video analiz hatası ({video_id}): {e}")

            # Hata durumunda fallback
            sizes = {q: "Bilinmiyor" for q in qualities}
            self._js(f"updatePlaylistItemSize({idx}, {json.dumps(sizes)})")

        try:
            with ThreadPoolExecutor(max_workers=3) as executor:
                for idx, entry in enumerate(entries):
                    if self.should_stop:
                        break
                    executor.submit(fetch_one, idx, entry)
        except Exception as e:
            logging.error(f"Playlist detay hatası: {e}")

    # ═══════════════════════════════════════════════════════════
    #  API: BOYUT SORGULAMA (fallback — ana boyut analyze'da gider)
    # ═══════════════════════════════════════════════════════════

    def get_size(self, quality, url=""):
        """JS'den çağrılır — setQuality fallback'i için."""
        if not self.last_info:
            return None
        if 'list=' in url:
            return "Hesaplanıyor..."
        val = self._calc_size(self.last_info, quality)
        return f"{val} MB" if val else "Bilinmiyor"

    # ═══════════════════════════════════════════════════════════
    #  API: KLASÖR SEÇME
    # ═══════════════════════════════════════════════════════════

    def browse(self):
        try:
            if not self.window:
                return None
            result = self.window.create_file_dialog(webview.FOLDER_DIALOG)
            if result and len(result) > 0:
                self.download_path = result[0]
                safe = self.download_path.replace("\\", "/")
                return safe
            return None
        except Exception as e:
            logging.error(f"Klasör seçme hatası: {e}\n{traceback.format_exc()}")
            return None

    def _parse_time_str(self, time_str):
        """'0:03', '00:03', '3', '1:15', '01:15:30' gibi metinleri saniyeye dönüştürür."""
        if not time_str or not time_str.strip():
            return None
        time_str = time_str.strip()
        try:
            if ':' in time_str:
                parts = time_str.split(':')
                if len(parts) == 2:
                    mins, secs = parts
                    return float(mins) * 60 + float(secs)
                elif len(parts) == 3:
                    hrs, mins, secs = parts
                    return float(hrs) * 3600 + float(mins) * 60 + float(secs)
            return float(time_str)
        except Exception:
            return None

    # ═══════════════════════════════════════════════════════════
    #  API: İNDİRME
    # ═══════════════════════════════════════════════════════════

    def download(self, url, quality, path=None, format_type="mp4", start_time="", end_time=""):
        if not url:
            return
        if not path or not path.strip():
            path = self.download_path
        self.should_stop = False
        self.pause_event.set()
        threading.Thread(
            target=self._download_thread,
            args=(url, quality, path, start_time, end_time),
            daemon=True,
        ).start()

    def _download_thread(self, url, quality, path, start_time="", end_time=""):
        ffmpeg_path = os.path.join(self.base_path, "ffmpeg.exe")

        # Playlist ise alt klasör oluştur
        is_playlist = 'list=' in url
        if is_playlist:
            try:
                import yt_dlp
                with yt_dlp.YoutubeDL(self._ydl_opts(url=url, extract_flat=True)) as ydl:
                    pl_info = ydl.extract_info(url, download=False)
                    pl_title = pl_info.get('title', 'Playlist')
                    # Geçersiz dosya adı karakterlerini temizle
                    for ch in '<>:"/\\|?*':
                        pl_title = pl_title.replace(ch, '_')
                    path = os.path.join(path, pl_title)
                    os.makedirs(path, exist_ok=True)
            except Exception as e:
                logging.error(f"Playlist klasör hatası: {e}")

        self.last_downloaded_path = path

        # Zaman aralığı kesme hesaplama
        start_sec = self._parse_time_str(start_time)
        end_sec = self._parse_time_str(end_time)
        has_trim = start_sec is not None or end_sec is not None

        trim_tag = ""
        if has_trim:
            s_label = f"{int(start_sec)}s" if start_sec is not None else "0s"
            e_label = f"{int(end_sec)}s" if end_sec is not None else "son"
            trim_tag = f" [{s_label}-{e_label}]"

        # Çözünürlük ve kesme etiketli dosya adı şablonu
        if quality == "audio":
            filename_tmpl = f'%(title)s{trim_tag} [MP3].%(ext)s'
        else:
            filename_tmpl = f'%(title)s{trim_tag} [{quality}p].%(ext)s'

        ydl_opts = self._ydl_opts(
            url=url,
            outtmpl=os.path.join(path, filename_tmpl),
            progress_hooks=[self._progress_hook],
            ffmpeg_location=ffmpeg_path,
            continuedl=True,
            overwrites=True,
            noplaylist=not is_playlist,
            lazy_playlist=True,
            ignoreerrors=True,
        )

        if has_trim:
            from yt_dlp.utils import download_range_func
            s_val = start_sec if start_sec is not None else 0
            e_val = end_sec if end_sec is not None else float('inf')
            ydl_opts['download_ranges'] = download_range_func(None, [(s_val, e_val)])
            ydl_opts['force_keyframes_at_cuts'] = True

        if quality == "audio":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            ydl_opts.update({
                'format': f'bestvideo[height<={quality}]+bestaudio/best',
                'merge_output_format': 'mp4',
                'postprocessor_args': {
                    'merger': ['-c', 'copy'],   # Remux — codec dönüşümü yok
                },
            })

        try:
            import yt_dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            if self.should_stop:
                self._js(f"finishDownload(false, {json.dumps('⚠️ İptal edildi.')})")
            else:
                self._js(f"finishDownload(true, {json.dumps('✅ İndirme Başarıyla Tamamlandı!')})")

        except Exception as e:
            if type(e).__name__ == "DownloadCancelled":
                self._js(f"finishDownload(false, {json.dumps('⚠️ İptal edildi.')})")
            else:
                logging.error(f"İndirme hatası: {e}\n{traceback.format_exc()}")
                self._js(f"finishDownload(false, {json.dumps('❌ İndirme Hatası! Detaylar: indirici_hata.log')})")

    def _progress_hook(self, d):
        """yt-dlp ilerleme hook'u — duraklatma ve durdurma kontrolü yapar."""
        # Duraklatma
        self.pause_event.wait()

        # Durdurma
        if self.should_stop:
            import yt_dlp
            raise yt_dlp.utils.DownloadCancelled("STOP_REQUESTED")

        if d['status'] != 'downloading' or not self.window:
            return

        try:
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            if total <= 0:
                return

            percent = (downloaded / total) * 100

            # Saniyede maksimum 3 kez UI güncelle (IPC ve WebView2 kilitlenmelerini önler)
            import time
            now = time.time()
            if now - self._last_progress_time < 0.3 and percent < 100:
                return
            self._last_progress_time = now

            # Hız
            speed = d.get('speed') or 0
            speed_str = ""
            if speed > 0:
                if speed > 1024 * 1024:
                    speed_str = f" — {speed / (1024 * 1024):.1f} MB/s"
                else:
                    speed_str = f" — {speed / 1024:.0f} KB/s"

            # ETA
            eta = d.get('eta') or 0
            eta_str = ""
            if eta > 0:
                if eta >= 60:
                    eta_str = f" | ~{eta // 60}dk {eta % 60}sn"
                else:
                    eta_str = f" | ~{eta}sn"

            # Playlist bilgisi
            info = d.get('info_dict', {})
            pl_index = info.get('playlist_index')
            pl_total = info.get('n_entries')

            status = f"İndiriliyor: %{int(percent)}{speed_str}{eta_str}"

            if pl_index is not None and pl_total is not None:
                self._js(
                    f"updateProgress({percent}, {json.dumps(status)}, "
                    f"{int(pl_index)}, {int(pl_total)})"
                )
            else:
                self._js(f"updateProgress({percent}, {json.dumps(status)})")
        except Exception:
            pass

    # ═══════════════════════════════════════════════════════════
    #  API: KONTROLLER
    # ═══════════════════════════════════════════════════════════

    def open_download_folder(self, path=None):
        target_path = self.last_downloaded_path if (self.last_downloaded_path and os.path.exists(self.last_downloaded_path)) else path
        if not target_path:
            return
        target_path = os.path.normpath(target_path)
        if not os.path.exists(target_path):
            logging.warning(f"Açılacak dizin bulunamadı: {target_path}")
            return
        try:
            if os.name == 'nt':
                os.startfile(target_path)
            else:
                import subprocess
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.Popen([opener, target_path])
        except Exception as e:
            logging.error(f"Klasör açılırken hata: {e}")


    def stop_download(self):
        self.should_stop = True
        self.pause_event.set()   # Beklemedeyse çıkar

    def toggle_pause(self):
        if self.pause_event.is_set():
            self.pause_event.clear()
            return True     # Paused
        else:
            self.pause_event.set()
            return False    # Resumed

    def restart_app(self):
        import subprocess
        if self.window:
            try:
                self.window.destroy()
            except Exception:
                pass

        if getattr(sys, 'frozen', False):
            exe = sys.executable
            cmd = f'cmd /c "ping 127.0.0.1 -n 3 >nul & start "" "{exe}""'
        else:
            bat = os.path.join(self.base_path, "baslat.bat")
            if os.path.exists(bat):
                cmd = f'cmd /c "ping 127.0.0.1 -n 3 >nul & start "" "{bat}""'
            else:
                py = os.path.abspath(sys.argv[0])
                cmd = f'cmd /c "ping 127.0.0.1 -n 3 >nul & start "" python "{py}""'

        subprocess.Popen(cmd, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        os._exit(0)


# ═══════════════════════════════════════════════════════════════
#  ANA GİRİŞ
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    try:
        api = EliteApi()

        # Dosya yollarını belirle (PyInstaller uyumlu)
        html_file = resource_path('index.html')
        css_file  = resource_path('index.css')
        js_file   = resource_path('index.js')
        logo_file = resource_path('logo.png')
        icon_file = resource_path('logo.ico')

        if not os.path.exists(html_file):
            base_dir = os.path.dirname(os.path.realpath(__file__))
            html_file = os.path.join(base_dir, 'index.html')
            css_file  = os.path.join(base_dir, 'index.css')
            js_file   = os.path.join(base_dir, 'index.js')
            logo_file = os.path.join(base_dir, 'logo.png')
            icon_file = os.path.join(base_dir, 'logo.ico')

        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # CSS enjekte et
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                css = f.read()
            html_content = html_content.replace('<!-- STYLESHEET_PLACEHOLDER -->', f'<style>\n{css}\n</style>')

        # JS enjekte et
        if os.path.exists(js_file):
            with open(js_file, 'r', encoding='utf-8') as f:
                js = f.read()
            html_content = html_content.replace('<!-- SCRIPT_PLACEHOLDER -->', f'<script>\n{js}\n</script>')

        # Logo base64 enjekte et
        if os.path.exists(logo_file):
            with open(logo_file, 'rb') as f:
                logo_b64 = base64.b64encode(f.read()).decode()
            logo_data = f'data:image/png;base64,{logo_b64}'
            html_content = html_content.replace('src="logo.png"', f'src="{logo_data}"')
            html_content = html_content.replace('let LOGO_DATA = "";', f'let LOGO_DATA = "{logo_data}";')

        # Sürüm numarasını HTML'e senkronize et
        html_content = html_content.replace('v1.2.0', f'v{__version__}')

        # Başlangıç değerlerini enjekte et (Pywebview on_loaded kilidini önlemek için)
        safe_path = api.download_path.replace("\\", "/")
        html_content = html_content.replace('>/Downloads/<', f'>{safe_path}<')
        
        if not os.path.exists(os.path.join(api.base_path, "ffmpeg.exe")):
            html_content = html_content.replace(
                'Sistem Durumu: Çalışıyor',
                '⚠️ UYARI: ffmpeg.exe bulunamadı! İndirmeler çalışmayabilir.'
            )

        # Dev HTML metnini geçici bir dosyaya yazarak IPC deadlock'ını engelle
        temp_dir = tempfile.gettempdir()
        temp_html_path = os.path.join(temp_dir, f"indirici_ui_{__version__}.html")
        with open(temp_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Pencere oluştur (url üzerinden yükleme IPC kilitlenmesini önler)
        window = webview.create_window(
            title=f'İndirici v{__version__}',
            url=f"file:///{temp_html_path.replace('\\', '/')}",
            js_api=api,
            width=1100,
            height=750,
            resizable=True,
            min_size=(900, 600),
            background_color='#131313',
        )
        api.window = window     # API'ye pencere referansı ver

        # DOM ve Window tam yüklendiğinde is_ready flag'ini aktif et
        def on_loaded():
            api.is_ready = True

        window.events.loaded += on_loaded

        # gui='edgechromium' argümanı çıkarıldı (ortam değişkeninden alınır, çakışmayı önler)
        webview.start(debug=False)

    except Exception as e:
        logging.critical(f"Uygulama çökme hatası: {e}\n{traceback.format_exc()}")