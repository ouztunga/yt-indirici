<!-- last_updated: 2026-07-27 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] İndirme bittiğinde arayüzün otomatik sıfırlanmasını engelleme.
* [x] "İNDİRİLEN KONUMU AÇ" ve "YENİ İNDİRME" butonlarının eklenmesi ve Python backend ile entegrasyonu.
* [x] Sub-agent ile kod kalitesi ve mantıksal UI durum çakışmalarının test edilip düzeltilmesi.
* [x] Değişikliklerin GitHub'a commit ve push edilmesi.

---

## 🔄 Son Değişiklikler (Recent Changes)

* **İndirme Sonu Arayüz Koruması & Klasör Açma:**
  * İndirme başarıyla tamamlandığında ekran artık 3 saniye sonra otomatik sıfırlanmıyor.
  * `index.html` ve `index.js` dosyalarına `finishControls` konteyneri eklendi.
  * İndirilen dosyanın/playlist'in bulunduğu klasörü tek tıkla işletim sisteminde açan `open_download_folder` metodu Python tarafında yazıldı (`os.path.normpath` ve `self.last_downloaded_path` takibi eklendi).
  * Yeni video linki yapıştırıldığında veya "YENİ İNDİRME" butonuna tıklandığında UI durumu düzgünce sıfırlanıp hazırlanıyor.


---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Local `cookies.txt` Önceliği:**
  * Modern tarayıcılar (Chrome 127+) Windows DPAPI şifrelemesini sıkılaştırdığından, kilitli durumlar için kullanıcı odaklı `cookies.txt` desteği en kararlı ve kesintisiz fallback olarak seçilmiştir.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] `derle.bat` arka plan işleminin tamamlanmasının doğrulanması.
* [ ] Kullanıcının güncellenmiş `indirici.exe` uygulamasını test etmesi.
