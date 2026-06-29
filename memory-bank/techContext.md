# 🛠️ Tech Context / Teknik Bağlam

> **AI Instruction:** Bu dosya tam teknoloji yığınını, geliştirme ortamlarını, harici bağımlılıkları ve çalıştırma/derleme komutlarını içerir. Bu kurallara ve sınırlara harfiyen uyun.

---

## 💻 Teknoloji Yığını ve Sürümler (Tech Stack & Versions)

* **Dil (Language):** Python 3.12 (Windows 11 uyumluluğu ve kararlılık için zorunludur)
* **Arayüz Motoru (GUI Engine):** `pywebview` (Edge Chromium / WebView2 arka uçlu)
* **İndirme Mantığı (Download Core):** `yt-dlp` (YouTube API ve indirme akışları için en güncel sürüm)
* **Post-Processing (Ses/Video Birleştirme):** `ffmpeg.exe` (Ses/Video remux ve MP3 çıkarma için)
* **Derleme Aracı (Build Tool):** `PyInstaller` (Tek bir taşınabilir EXE üretmek için)

---

## 🚀 Yerel Çalıştırma ve Derleme Komutları (Local Development Commands)

* **Uygulamayı Python ile Çalıştırma:**
  Uygulamanın olduğu dizinde komut satırından `baslat.bat` dosyasını çalıştırın:
  ```cmd
  baslat.bat
  ```
  *(Bu dosya Python 3.12 ile `indirici.py` dosyasını başlatır.)*

* **Uygulamayı EXE Olarak Derleme (Build):**
  Uygulamayı tek bir bağımsız yürütülebilir dosyaya dönüştürmek için `derle.bat` çalıştırın:
  ```cmd
  derle.bat
  ```
  *(Bu dosya eski derlemeleri temizler ve PyInstaller ile index.html ile logoları içine gömerek `indirici.exe` dosyasını ana dizine kopyalar.)*

---

## 🔒 Teknik Sınırlar ve Korumalar (Technical Constraints & Guardrails)

* **Erişilebilirlik Kilitlenme Çözümü (Accessibility Workaround):**
  Windows 11 işletim sistemlerinde WebView2'nin donmasını önlemek için aşağıdaki çevre değişkenleri kodun en başında set edilmelidir:
  ```python
  sys.setrecursionlimit(20000)
  os.environ['PYWEBVIEW_GUI'] = 'edgechromium'
  os.environ['WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS'] = '--disable-renderer-accessibility'
  ```
* **PyInstaller Dosya Yolları (Resource Pathing):**
  Arayüzün (`index.html`) ve simgelerin EXE içerisinden çalışırken bulunabilmesi için `resource_path` fonksiyonu kullanılmalıdır:
  ```python
  def resource_path(relative_path):
      try:
          base_path = sys._MEIPASS
      except Exception:
          base_path = os.path.dirname(os.path.realpath(__file__))
      return os.path.join(base_path, relative_path)
  ```
* **FFmpeg Bağımlılığı (FFmpeg Dependency):**
  `ffmpeg.exe` dosyası uygulamanın çalıştığı ana dizinde veya sistem yolunda (PATH) yer almalıdır. Aksi takdirde video birleştirme ve ses dönüştürme işlemleri başarısız olur. Program açılışta bunun kontrolünü yapar ve arayüzde uyarı verir.
