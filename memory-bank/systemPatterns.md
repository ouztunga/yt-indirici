# 🧬 System Patterns / Sistem Kalıpları

> **AI Instruction:** Bu dosya, sistem mimarisini, dizin yapılarını, tasarım desenlerini ve temel teknik kararları belgeler. Kodun düzenli, modüler ve tutarlı kalması için bu kuralları takip edin.

---

## 🏛️ Teknik Mimari (Technical Architecture)

YT İndirici, Python ve JavaScript arasında iki yönlü iletişime dayalı hibrit bir masaüstü uygulamasıdır.

* **Arayüz (Frontend):** Modern karanlık tema (Dark UI), TailwindCSS/CSS3, vanilya JavaScript. `index.html` dosyası içinde tüm UI ve stil tanımları tek bir yerde toplanmıştır.
* **Arka Plan (Backend):** Python 3.12, `pywebview` kütüphanesi ile pencere yönetimi ve yerel işletim sistemi entegrasyonu (klasör seçme, uygulama kapatma, yeniden başlatma).
* **İndirme Motoru:** `yt-dlp` kütüphanesi ve video/ses birleştirme/dönüştürme işleri için `ffmpeg.exe` programı.
* **İletişim Köprüsü:** `webview.create_window` aracılığıyla JavaScript tarafına aktarılan `EliteApi` sınıfı. Python'dan JS'e bilgi gönderilirken, parametre kaçış (escape) hatalarını önlemek için her zaman `json.dumps()` kullanılır.

---

## 📂 Dizin Yapısı (Directory Structure)

```text
YT İndirici/
├── .cursor/rules/             # AI ajan kuralları (vibe-core, tech-stack, planning)
├── .github/                   # GitHub/Copilot entegrasyon ayarları
├── memory-bank/               # Proje bellek dosyaları (activeContext, progress, etc.)
├── vibecoding/                # Vibe coding şablon yedekleri ve kılavuzları
├── baslat.bat                 # Uygulamayı Python ile doğrudan başlatan Windows betiği
├── derle.bat                  # PyInstaller ile tek EXE haline getiren derleme betiği
├── ffmpeg.exe                 # Video ve ses birleştirme için gereken ikili dosya (git-ignored)
├── ffplay.exe / ffprobe.exe   # Yardımcı FFmpeg araçları (git-ignored)
├── index.html                 # Kullanıcı arayüzü dosyası (PyInstaller ile EXE içine gömülür)
├── indirici.py                # Tüm Python kodunu, API'leri ve indirme mantığını içeren ana dosya
├── indirici_hata.log          # Python tarafında oluşan çalışma zamanı hata kayıtları
├── indirilenler_gecmisi.txt   # Çift indirmeleri önleyen yt-dlp arşivi
├── logo.ico / logo.png        # Uygulama simgeleri ve logoları (EXE içine gömülür)
└── size_cache.json            # Çözünürlüklere göre video/ses boyut önbelleği
```

---

## 🛡️ Kritik Tasarım Kalıpları (Crucial Design Patterns)

1. **İlişkisel Döngü Koruması (Non-Circular Window Reference):**
   * GUI ile API mantığı arasında dairesel referans oluşmasını engellemek için `EliteApi` içinde pencere referansı tutulmaz. Bunun yerine modül seviyesinde global bir `MAIN_WINDOW` değişkeni kullanılır.
2. **Çoklu İş Parçacığı Yönetimi (Multithreading):**
   * Arayüzün donmaması için tüm ağır işlemler (Link analizi, İndirme, Playlist video boyutlarını alma) arka planda daemon thread'ler olarak çalıştırılır.
   * Playlist boyut analizinde sistemin kilitlenmesini önlemek için 3 işçi limitli `ThreadPoolExecutor` kullanılır.
3. **Önbellekleme Mantığı (Caching Pattern):**
   * Aynı YouTube linki ve kalitesi tekrar sorgulandığında yt-dlp'nin zaman alıcı analiz sürecini atlamak için sorgu sonuçları `size_cache.json` dosyasına yazılır ve okunur.
4. **Hata Dayanıklılığı (Resilience):**
   * Video indirmelerinde veya playlist taramalarında `ignoreerrors: True` kullanılarak hatalı/silinmiş videoların tüm süreci bozması engellenir.
