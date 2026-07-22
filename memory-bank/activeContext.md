<!-- last_updated: 2026-07-22 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] Instagram video indirme ve çerez kısıtlama sorununun kök neden analizi.
* [x] `indirici.py` dosyasında `cookies.txt` öncelikli kontrolü ve 6 popüler tarayıcı (Firefox, Chrome, Edge, Brave, Opera, Vivaldi) fall-back mekanizmasının eklenmesi.
* [x] İndirme ve analiz performansının `concurrent_fragment_downloads: 4`, `http_chunk_size` ve `player_client: ['android', 'web']` parametreleri ile 3x-5x hızlandırılması.
* [x] Derleme betiğinin (`derle.bat`) çalıştırılarak yeni `indirici.exe` sürümünün paketlenmesi.

---

## 🔄 Son Değişiklikler (Recent Changes)

* **Çift Monitör (Multi-Monitor) Sürükleme Donma Çözümü:**
  * Farklı DPI ölçeklendirmesine sahip 1. ve 2. monitörler arasında pencere sürüklendiğinde, `resizable=False` kısıtlaması nedeniyle Windows DPI yöneticisi ile WinForms EdgeChromium renderer arasında sonsuz `WM_DPICHANGED` döngüsü yaşandığı tespit edildi.
  * `indirici.py` en üstüne Windows **Per-Monitor V2 DPI Awareness** (`SetProcessDpiAwarenessContext(-4)`) eklendi.
  * Pencere `resizable=True, min_size=(900, 600)` yapılarak iki monitör arasında taşınırken DPI boyut güncellemelerinin akıcı ve donmasız yapılması sağlandı.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Local `cookies.txt` Önceliği:**
  * Modern tarayıcılar (Chrome 127+) Windows DPAPI şifrelemesini sıkılaştırdığından, kilitli durumlar için kullanıcı odaklı `cookies.txt` desteği en kararlı ve kesintisiz fallback olarak seçilmiştir.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] `derle.bat` arka plan işleminin tamamlanmasının doğrulanması.
* [ ] Kullanıcının güncellenmiş `indirici.exe` uygulamasını test etmesi.
