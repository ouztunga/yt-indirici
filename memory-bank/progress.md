<!-- last_updated: 2026-06-06 -->
# 📈 Progress Tracker / İlerleme Takipçisi

> **AI Instruction:** Bu dosya projenin yol haritasıdır. Tamamlanan özellikleri, bekleyen maddeleri ve bilinen hataları takip eder. Görevler tamamlandıkça bu dosyayı güncel tutun.

---

## 🛠️ Proje Yol Haritası (Project Roadmap)

### Tamamlanan Özellikler (Completed Features) ✅
*   [x] Python 3.12 geçişi tamamlandı (Windows 11 kararlılığı).
*   [x] Dairesel referans kilitlenmesi (circular reference recursion) giderildi.
*   [x] `create_window` TypeError (icon parametresi) hatası çözüldü.
*   [x] Windows 11 Erişilebilirlik kilitlenme döngüsü engellendi (`--disable-renderer-accessibility`).
*   [x] Dosya isimleri küçük harfe standartlaştırıldı (`indirici.py`, `index.html`).
*   [x] Duraklatma, Devam Ettirme ve İndirmeyi İptal Etme (Pause/Resume/Stop) özellikleri eklendi.
*   [x] pywebview-JS iletişim köprüsü `json.dumps` serileştirmesi ile güçlendirildi.
*   [x] Uygulama başlangıcında `ffmpeg.exe` varlığı kontrolü eklendi ve arayüzde uyarı verilmesi sağlandı.
*   [x] Dil desteği basitleştirildi; sadece Türkçe olarak ayarlandı.
*   [x] İndirme formatı basitleştirildi; MKV kaldırıldı, hızlı MP4 remuxing varsayılan yapıldı.
*   [x] Playlist indirme çökmeleri engellendi; silinmiş/gizli videoları atlamak için `ignoreerrors` eklendi.
*   [x] Playlist video boyutlarının arka planda paralel thread ile dinamik taranması ve UI'da canlı gösterimi sağlandı.
*   [x] Dosya boyutu hesaplamasındaki tutarsızlıklar giderildi (en yüksek kaliteli ses akışı seçilerek birleştirilen boyutlar doğru hesaplandı).
*   [x] **Vibe Coding Entegrasyonu:** Proje kuralları, yoksayma listeleri ve yapılandırma dosyaları son gelen `vibecoding_yeni` klasöründeki güncel şablona göre güncellendi.
*   [x] **Fallow (Codebase Intelligence) Entegrasyonu:** Fallow kod zekası entegrasyonu tamamlandı, Claude Code için `.claude` altındaki `/fallow` komut ve yetenek (skill) şablonları eklendi.
*   [x] **Temizlik:** Güncelleme sonrasında geçici `vibecoding` ve yeni iletilen `vibecoding_yeni` klasörleri silinerek çalışma alanı temiz tutuldu.
*   [x] **Arayüz Modülerizasyonu:** Monolitik `index.html` (624 satır) dosyası HTML, CSS (`index.css`) ve JS (`index.js`) olarak modülerleştirildi. Satır limiti standartlarına uyuldu. `indirici.py` ve `derle.bat` dosyaları bu yapıya göre güncellendi.

### Bekleyen Özellikler (Pending Features) ⏳
*   [ ] İndirme motorunun kararlılığının son kez test edilmesi (`baslat.bat` üzerinden).
*   [ ] Fallow'un tespit ettiği JS tekrarlarının giderilmesi (refactoring).
*   [ ] Toplu indirme (batch download) desteği eklenmesi.
*   [ ] Arayüzde karanlık/aydınlık tema (dark/light mode) geçiş düğmesi eklenmesi.
*   [ ] Yeni kodlar ve düzeltmelerle birlikte nihai `indirici.exe` derlemesinin yapılması.

---

## 🐛 Bilinen Hatalar ve Engeller (Known Issues & Blockages)
*   **Çözüldü:** `get_size()` deadlock hatası — URL artık parametre olarak alınıyor, evaluate_js bloklanması ortadan kalktı.
*   **Çözüldü:** CSS scrollbar çakışması — `custom-scroll` artık görünür.
*   **Çözüldü:** Logo base64 modal hatası — LOGO_DATA karşılaştırması ile önlendi.
*   **Çözüldü:** `download()` path güvenliği — fallback olarak `self.download_path` kullanılıyor.
*   **Çözüldü:** Playlist modunda `updateSizeIfMatch` anlamsız güncelleme — `isPlaylistActive` kontrolü eklendi.
*   **Bilinen Hata:** ffmpeg.exe dosyası çalışma dizininde olmadığında video birleştirmeleri başarısız olur (Arayüzde uyarı veriliyor).

---

## 📊 Yapım İstatistikleri (Summary of Build Metrics)
*   **Durum (Status):** 🚀 Arayüz Modüler Yapıya Geçti. Derleme Başarıyla Doğrulandı.
*   **Yüklenen Kurallar (Engine Rules):** 3 Modüler kural dosyası, 4 evrensel editör kuralı.
*   **Hafıza Durumu (Memory State):** Aktif ve güncel.
