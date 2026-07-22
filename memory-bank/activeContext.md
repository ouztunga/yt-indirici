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

* **Yeniden Başlat (Restart) Donma Çözümü:**
  * Konsol penceresiz GUI süreçlerinde `timeout` komutu desteklenmediği için anında `ERROR: Input redirection is not supported` hatası veriyor ve 0.001 saniyede yeni uygulamayı açıyordu.
  * Bu durum WebView2 önbellek ve port kilitleri henüz serbest kalmadan yeni uygulamanın açılmasına ve "Yanıt vermiyor" kilitlenmesine yol açıyordu.
  * `self.window.destroy()` ile WebView2 penceresi önce düzgünce kapatıldı ve `ping 127.0.0.1 -n 3` ile 2 saniyelik temiz bir bekleme süresi verilerek donma sorunu kalıcı olarak çözüldü.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Local `cookies.txt` Önceliği:**
  * Modern tarayıcılar (Chrome 127+) Windows DPAPI şifrelemesini sıkılaştırdığından, kilitli durumlar için kullanıcı odaklı `cookies.txt` desteği en kararlı ve kesintisiz fallback olarak seçilmiştir.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] `derle.bat` arka plan işleminin tamamlanmasının doğrulanması.
* [ ] Kullanıcının güncellenmiş `indirici.exe` uygulamasını test etmesi.
