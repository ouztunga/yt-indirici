<!-- last_updated: 2026-09-16 -->
# 📈 Progress Tracker / İlerleme Takipçisi

> **AI Instruction:** Bu dosya projenin yol haritasıdır. Tamamlanan özellikleri, bekleyen maddeleri ve bilinen hataları takip eder. Görevler tamamlandıkça bu dosyayı güncel tutun.

---

## 🛠️ Proje Yol Haritası (Project Roadmap)

### Tamamlanan Özellikler (Completed Features) ✅
*   [x] Python 3.12 geçişi tamamlandı (Windows 11 kararlılığı).
*   [x] Dairesel referans kilitlenmesi (circular reference recursion) giderildi.
*   [x] `create_window` TypeError (icon parametresi) hatası çözüldü.
*   [x] Windows 11 Erişilebilirlik kilitlenme döngüsü engellendi (`--disable-renderer-accessibility`).
*   [x] Windows 11 Erişilebilirlik (Accessibility) kilitlenme hatası çözüldü (sys.setrecursionlimit kaldırıldı ve pywebview susturuldu).
*   [x] Dosya isimleri küçük harfe standartlaştırıldı (`indirici.py`, `index.html`).
*   [x] Duraklatma, Devam Ettirme ve İndirmeyi İptal Etme (Pause/Resume/Stop) özellikleri eklendi.
*   [x] pywebview-JS iletişim köprüsü `json.dumps` serileştirmesi ile güçlendirildi.
*   [x] Uygulama başlangıcında `ffmpeg.exe` varlığı kontrolü eklendi ve arayüzde uyarı verilmesi sağlandı.
*   [x] Dil desteği basitleştirildi; sadece Türkçe olarak ayarlandı.
*   [x] İndirme formatı basitleştirildi; MKV kaldırıldı, hızlı MP4 remuxing varsayılan yapıldı.
*   [x] Playlist indirme çökmeleri engellendi; silinmiş/gizli videoları atlamak için `ignoreerrors` eklendi.
*   [x] Playlist video boyutlarının arka planda paralel thread ile dinamik taranması ve UI'da canlı gösterimi sağlandı.
*   [x] Dosya boyutu hesaplamasındaki tutarsızlıklar giderildi (en yüksek kaliteli ses akışı seçilerek birleştirilen boyutlar doğru hesaplandı).
*   [x] **Instagram ve Sosyal Medya İndirme Desteği:** `cookies.txt` öncelikli kontrolü ile 6 popüler tarayıcı (Firefox, Chrome, Edge, Brave, Opera, Vivaldi) fall-back ve hata yakalama mekanizması eklendi.
*   [x] **Windows 11 Başlat Arama İndeksi:** Start Menu Programs altına `YT Indirici.lnk` kısayolu yerleştirildi; `yt in` aramasında anında bulunup başlatılabiliyor.
*   [x] **PUSH → PULL Hibrit Mimarisi:** Arka plan worker thread'lerindeki tüm `evaluate_js` çağrıları kaldırıldı; thread-safe state dict + version sayacı kuruldu.
*   [x] **pywebview Reflection Deadlock Çözümü:** `EliteApi` nesnesinin dahili nitelikleri (`_window`, `_pause_event` vb.) private yapılarak .NET WinForms COM teftiş kilitlenmesi tamamen ortadan kaldırıldı; açılışta ve çalışma esnasında %100 responsive (`Responding = True`) sağlandı.

### Bekleyen Özellikler (Pending Features) ⏳
*   [ ] Oğuz'un YouTube / Instagram / TikTok indirmelerini canlıda denemesi.
*   [ ] Toplu indirme (batch download) desteği eklenmesi.
*   [ ] Arayüzde karanlık/aydınlık tema (dark/light mode) geçiş düğmesi eklenmesi.

---

## 🐛 Bilinen Hatalar ve Engeller (Known Issues & Blockages)
*   **Çözüldü:** `get_size()` deadlock hatası — URL artık parametre olarak alınıyor, evaluate_js bloklanması ortadan kalktı.
*   **Çözüldü:** CSS scrollbar çakışması — `custom-scroll` artık görünür.
*   **Çözüldü:** Logo base64 modal hatası — LOGO_DATA karşılaştırması ile önlendi.
*   **Çözüldü:** `download()` path güvenliği — fallback olarak `self.download_path` kullanılıyor.
*   **Çözüldü:** Playlist modunda `updateSizeIfMatch` anlamsız güncelleme — `isPlaylistActive` kontrolü eklendi.
*   **Çözüldü:** Windows 11 Accessibility/EdgeChromium circular log çökmesi — pywebview logger susturuldu.
*   **Bilinen Hata:** ffmpeg.exe dosyası çalışma dizininde olmadığında video birleştirmeleri başarısız olur (Arayüzde uyarı veriliyor).

---

## 📊 Yapım İstatistikleri (Summary of Build Metrics)
*   **Durum (Status):** 🚀 Tüm Düzeltmeler Tamamlandı, EXE Başarıyla Paketlendi ve GitHub'a Yüklendi.
*   **Yüklenen Kurallar (Engine Rules):** 3 Modüler kural dosyası, 4 evrensel editör kuralı.
*   **Hafıza Durumu (Memory State):** Aktif ve güncel.
