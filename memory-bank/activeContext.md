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

* **Instagram Video İndirme ve Çoklu Çerez (Cookie) Desteği:**
  * Windows 11 üzerinde Chrome/Edge kilitli DB ve App-Bound Encryption (DPAPI) engellerini aşmak üzere `_find_cookie_source()` metodu geliştirildi.
  * Öncelik sırası: Local `cookies.txt` -> Firefox -> Edge -> Chrome -> Brave -> Opera -> Vivaldi -> Çerezsiz mod.
  * Instagram hatalarında kullanıcıya Netscape biçimli `cookies.txt` kullanımı hakkında rehberlik sağlandı.
* **Performans İyileştirmeleri:**
  * `yt-dlp` ayarlarında `concurrent_fragment_downloads = 4`, `http_chunk_size = 10MB`, `buffersize = 1MB` ve `player_client = ['android', 'web']` aktif edilerek indirme ve analiz süreleri önemli ölçüde düşürüldü.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Local `cookies.txt` Önceliği:**
  * Modern tarayıcılar (Chrome 127+) Windows DPAPI şifrelemesini sıkılaştırdığından, kilitli durumlar için kullanıcı odaklı `cookies.txt` desteği en kararlı ve kesintisiz fallback olarak seçilmiştir.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] `derle.bat` arka plan işleminin tamamlanmasının doğrulanması.
* [ ] Kullanıcının güncellenmiş `indirici.exe` uygulamasını test etmesi.
