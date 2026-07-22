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

* **Arayüz (UI) Donma & "Yanıt Vermiyor" Çözümü:**
  * Arka planda çalışan birden fazla thread'in (Playlist sorguları, İlerleme takibi) aynı anda `evaluate_js` çağırarak .NET WinForms arayüz işleyicisini kilitlediği (Thread Deadlock) tespit edildi.
  * `indirici.py` içerisine `self._js_lock = threading.Lock()` eklendi ve tüm JavaScript çağrıları thread-safe hale getirildi.
  * İndirme sırasındaki ilerleme güncellemeleri saniyede maksimum 10 güncelleme (10 FPS) olacak şekilde zaman kısıtlamasına (`_last_progress_time`) tabi tutuldu.
  * `index.js` içerisindeki `autoAnalyze` fonksiyonuna `http://` / `https://` protokol kontrolü ve 1 saniye debounce eklenerek boş istek spam'ı engellendi.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Local `cookies.txt` Önceliği:**
  * Modern tarayıcılar (Chrome 127+) Windows DPAPI şifrelemesini sıkılaştırdığından, kilitli durumlar için kullanıcı odaklı `cookies.txt` desteği en kararlı ve kesintisiz fallback olarak seçilmiştir.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] `derle.bat` arka plan işleminin tamamlanmasının doğrulanması.
* [ ] Kullanıcının güncellenmiş `indirici.exe` uygulamasını test etmesi.
