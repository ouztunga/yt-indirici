<!-- last_updated: 2026-06-06 -->
# 📋 Project Brief / Proje Özeti

> **AI Instruction:** Bu dosya, projenin temel hedefleri, kapsamı ve vizyonu için tek doğru kaynaktır. Genel hedefler değiştikçe bu belgeyi güncel tutun.

---

## 🎯 Temel Vizyon ve Kapsam (Core Vision & Scope)

* **Vizyon:** YT İndirici, Windows işletim sisteminde çalışan, yt-dlp tabanlı, hızlı, kararlı ve son derece şık/modern bir YouTube video ve ses indirme programıdır.
* **Kapsam:** YouTube linklerini analiz eden, tekli video/ses veya oynatma listelerini (playlist) arka planda indiren, indirme işlemlerini duraklatma/devam ettirme/iptal etme özelliklerine sahip olan ve WebView2 motoruyla çalışan bir masaüstü uygulamasıdır.

---

## 🚀 Temel Gereksinimler ve Hedefler (Key Requirements & Core Goals)

* **Hedef 1 (Kararlılık ve Bağımsızlık):** Windows 11 üzerinde donma ve erişilebilirlik hatalarını önlemek için özel parametrelerle (`--disable-renderer-accessibility`) ve Edge Chromium (WebView2) motoruyla çalışır. Harici bağımlılıkları tek bir EXE içinde (index.html ve logolar gömülü olarak) sunar.
* **Hedef 2 (Hızlı ve Verimli İndirme):** İndirilen MP4 videoları kod dönüştürmeden (remux) birleştirerek disk ve CPU tasarrufu sağlar. Ses indirmelerinde en yüksek kaliteli ses akışını (FFmpegExtractAudio ile MP3 formatında) çıkarır.
* **Hedef 3 (Playlist Desteği ve Hata Toleransı):** Oynatma listelerindeki özel, silinmiş veya erişilemeyen videoları otomatik atlar (`ignoreerrors`). Playlist içindeki videoların boyutlarını arka planda ThreadPoolExecutor ile paralel sorgulayarak arayüze gerçek zamanlı aktarır.
* **Hedef 4 (Kullanıcı Dostu Arayüz - UX/UI):** Kullanıcılara indirme hızı, ilerleme yüzdesi, ETA (kalan süre) ve oynatma listesi durumunu canlı güncellemelerle gösterir. İndirme klasörü seçimi için yerel bir diyalog penceresi sunar.

---

## 👥 Hedef Kitle ve Değer Önerisi (Target Audience & Value Proposition)

* **Hedef Kitle:** Terminal veya karmaşık komut satırı araçlarıyla (yt-dlp/ffmpeg) uğraşmak istemeyen, YouTube'dan yüksek hızlı video ve ses indirmek isteyen son kullanıcılar.
* **Değer Önerisi:** Kurulum gerektirmeyen taşınabilir yapı, indirme geçmişi kaydı, ffmpeg bütünlüğü kontrolü, duraklatma/iptal desteği ve tamamen Türkçe modern karanlık arayüz (Dark Mode).
