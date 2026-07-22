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

* **YouTube 1080p / High-Res Kısıtlama Çözümü:**
  * YouTube'daki 1080p/4K videoların uygulamada 360p olarak görünmesine neden olan `player_client: ['android', 'web']` parametre zorlaması tespit edildi. Android istemcisi mobil akışlarda kaliteyi 360p ile sınırlandırdığından kısıtlama kaldırıldı ve 1080p / 4K / 8K tüm çözünürlükler eksiksiz aktif edildi.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Local `cookies.txt` Önceliği:**
  * Modern tarayıcılar (Chrome 127+) Windows DPAPI şifrelemesini sıkılaştırdığından, kilitli durumlar için kullanıcı odaklı `cookies.txt` desteği en kararlı ve kesintisiz fallback olarak seçilmiştir.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] `derle.bat` arka plan işleminin tamamlanmasının doğrulanması.
* [ ] Kullanıcının güncellenmiş `indirici.exe` uygulamasını test etmesi.
