<!-- last_updated: 2026-09-07 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] İlk açılışta pencere sürüklenirken oluşan 5 saniyelik "(Yanıt Vermiyor)" donmasının giderilmesi.
* [x] Tailwind CSS'in harici CDN'den yerel `tailwind.min.js` dosyasına taşınması (sıfır ağ gecikmesi & offline render).
* [x] Pencerenin WebView2 ve DOM tam hazır olana kadar `hidden=True` başlayıp `on_loaded` ile ekrana getirilmesi.

---

## 🔄 Son Değişiklikler (Recent Changes)

* **Çerez Güvenliği ve Zırhlı İndirme:**
  * `_find_cookie_source()` fonksiyonunda açık tarayıcıların kilitli SQLite çerez dosyaları önceden test ediliyor, kilitliyse atlanıyor.
  * Açık sosyal medya linklerinde %99 oranında çerez gerekmediği için `none` (çerezsiz) mod önceliklendirildi.
  * İndirme sırasında herhangi bir çerez okuma/DPAPI hatası alınırsa işlem iptal edilmiyor; anında çerezleri sıfırlayıp doğrudan indirmeye geçiyor.
* **Saf Python + `.bat` Mimarisine Geçiş:**
  * `indirici.exe` (57 MB) ve `derle.bat`, `Yt-Indirici.spec` dosyaları Geri Dönüşüm Kutusu'na taşındı.
  * `.gitignore` güncellendi (`*.exe`, `*.spec`, `__pycache__/`).
  * `baslat.bat` içine çalışma dizini sabitlemesi (`cd /d "%~dp0"`) eklendi; doğrudan tıklandığında konsolsuz ve anında açılıyor.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Exe Yerine Doğrudan Script Çalıştırma:**
  * PyInstaller tekil exe paketleri Windows'ta her açılışta `%TEMP%` dizinine açıldığı için gecikme yaratıyordu ve her kod güncellemesinde 40 sn derleme süresi gerektiriyordu. Doğrudan `baslat.bat` / `pythonw` kullanılarak anında açılış, sıfır derleme süresi ve 0 false-positive sağlandı.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [x] Uygulamanın `baslat.bat` ile test edilmesi.
* [ ] Kullanıcının yeni indirmeleri denemesi.
