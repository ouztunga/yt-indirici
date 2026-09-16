<!-- last_updated: 2026-09-16 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] **Windows 11 Başlat Arama İndeksi:**
  * Masaüstündeki uygulamanın Windows 11 arama çubuğunda (`yt in`) anında bulunabilmesi için Start Menu Programs altına `YT Indirici.lnk` kısayolu yerleştirildi.
* [x] **Windows "(Yanıt Vermiyor)" IPC Deadlock Sorununun Kesin Çözümü (PUSH → PULL Hibrit Mimarisi):**
  * Tüm worker thread'lerden (`_analyze_thread`, `_download_thread`, `_progress_hook`) Windows Forms/COM mesaj kuyruğunu kilitleyen `window.evaluate_js()` çağrıları tamamen kaldırıldı.
  * Thread-safe merkezi state dictionary (`threading.Lock`) ve monotonik `version` takip mekanizması kuruldu (Asistan A).
  * Frontend tarafında (`index.js`), IPC çakışmalarını önleyen **recursive `setTimeout`** (~250ms) tabanlı `poll()` mekanizması kuruldu; sadece versiyon değiştiğinde DOM güncellenerek %100 akıcılık sağlandı (Asistan A).
  * Program boştayken gereksiz CPU tüketimini önleyen **Akıllı Polling Uyku Modu** ve `on_closing` temiz thread sonlandırma hook'u entegre edildi (Asistan B).
* [x] **Açılışta Donma / Ghost Window Kök Nedeninin Çözümü (pywebview Reflection Deadlock):**
  * pywebview'in `inject_pywebview` mekanizması, `EliteApi` üzerindeki `window`, `pause_event` gibi genel (public) nitelikleri arka plan thread'inde recursive olarak teftiş edip .NET WinForms / COM nesnelerine erişmeye çalıştığı için COM mesaj kuyruğu kilitleniyor ve pencere "Yanıt Vermiyor" durumuna düşüyordu.
  * Tüm dahili referanslar (`_window`, `_pause_event`, `_base_path`, `_download_path`, `_is_ready`, `_last_info`, `_should_stop`, `_last_downloaded_path`, `_last_working_cookie_mode`) private (`_`) yapıldı.
  * `index.js` içerisindeki kontrolsüz açılış polling'i yerine kullanıcı eylemine duyarlı on-demand polling'e geçildi.
  * PowerShell üzerinden arka arkaya test edildi; uygulama her açılış saniyesinde aralıksız `Responding = True` olarak çalışıyor.
  * Mevcut modern Bento Grid koyu tema tasarımı, 8K-1080p çözünürlük butonları, zaman kesme (trim) ve Premiere Pro H264/AAC postprocessor motoru eksiksiz korundu.

---

## 🔄 Son Değişiklikler (Recent Changes)

* **Git Checkpoint & Origin Senkronizasyonu:**
  * `cac84fe fix(deadlock): transition from push to pull hybrid architecture`
  * `b8acf34 checkpoint: remove accessibility disabling and fix pythonw stdio`
  * `fd92731 fix(deadlock): prevent pywebview reflection inspection deadlock on WinForms controls`
  * Tüm commit'ler GitHub `main` branch'ine başarıyla push edildi.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [x] Uygulamanın `baslat.vbs` ve Start Menu kısayolu ile açılış doğrulaması.
* [ ] Oğuz'un canlı video analiz ve indirme testi yapması.

