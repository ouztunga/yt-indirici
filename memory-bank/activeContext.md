<!-- last_updated: 2026-09-11 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] **Açılışta Donma ve "(Yanıt Vermiyor)" Hatasının Kesin Çözümü:**
  * Windows 11 UI Automation mesaj kuyruğu kilitlenmesini önlemek için `--disable-renderer-accessibility` argümanı eklendi.
  * GPU shader'larının her açılışta sıfırdan derlenmesini engelleyip diskte önbelleğe alınması için `--disable-gpu-shader-disk-cache` kaldırıldı.
  * 418 KB'lık hantal `tailwind.min.js` JIT derleyicisi tamamen kaldırılarak 22 KB'lık derlenmiş saf CSS (`index.css`) yapısına geçildi (HTML boyutu 805 KB'tan 392 KB'a indi).
  * `_js()` içindeki gereksiz `is_ready` kısıtı kaldırıldı, doğrudan pywebview'ın iç senkronizasyonuna devredildi.
  * Windows `IsHungAppWindow` API'si ile test edildi; uygulama açılış süresi 0.80 saniyeye düştü ve açılış anında tıklama/sürükleme sırasında sıfır takılma sağlandı.
* [x] **Kapsamlı Stabilite ve Performans Düzeltmesi (3 Paralel Denetim Sonrası):**
  * `_js_lock` ve 0.2s timeout mekanizması kaldırıldı (tüm UI donmaları ve kaybolan mesajlar çözüldü).
  * `player_skip: ['configs', 'webpage']` yt-dlp ayarlarından tamamen temizlendi (360p takılma sorunu çözüldü; 1080p, 1440p, 4K dahil tüm çözünürlükler geri geldi).
  * `gc.collect()` manuel çağrıları indirme döngüsünden temizlendi ("stop-the-world" UI duraksamaları yok edildi).
  * 11 adet fonksiyon içi tekrarlanan gereksiz import dosya başına taşındı.
  * `index.js` içindeki tüm pywebview API çağrıları try-catch blokları ile zırhlandı.
  * `renderPlaylistItems` DOM güncellemeleri DocumentFragment ile optimize edildi.

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
