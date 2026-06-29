<!-- last_updated: 2026-06-06 -->
# 🎨 Product Context / Ürün Bağlamı

> **AI Instruction:** Bu dosya, kullanıcı deneyiminin (UX) arkasındaki mantığı, temel kullanıcı senaryolarını ve uygulamanın genel işlevselliğini açıklar. Uygulamanın tasarımı ve hissinin (vibe) kullanıcının vizyonuyla uyumlu kalmasını sağlamak için bu belgeyi güncel tutun.

---

## 💡 Neden Bu Proje Var? (Why This Project Exists)

* **Problem Tanımı:** Mevcut YouTube indirme programlarının çoğu reklamlarla dolu, karmaşık arayüzlere sahip, kurulurken sisteme gereksiz yazılımlar bulaştıran veya komut satırı üzerinden çalıştığı için genel kullanıcılar için kullanımı zor olan araçlardır.
* **Değer Önerisi:** YT İndirici; tamamen ücretsiz, reklamsız, kurumsal kalitede modern karanlık arayüze sahip, duraklatma ve playlist desteği olan bağımsız (standalone) bir Windows programıdır.

---

## 🚶‍♂️ Temel Kullanıcı Senaryoları (Core User Journeys)

1. **Uygulamayı Açma ve Bağlantı Yapıştırma:**
   * Kullanıcı uygulamayı açar, indirme yolunun (varsayılan olarak İndirilenler klasörü) otomatik ayarlandığını görür.
   * YouTube'dan kopyaladığı tekli video veya playlist linkini arama kutusuna yapıştırır ve "Analiz Et" butonuna tıklar.
2. **Kalite Seçimi ve Boyut Bilgisi:**
   * Video analiz edildikten sonra videonun küçük resmi (thumbnail), başlığı ve çözünürlük seçenekleri (1080p, 720p, Ses vb.) belirir.
   * Seçilen kaliteye karşılık gelen dosya boyutu (Örn: 24.5 MB) gerçek zamanlı hesaplanarak ekranda gösterilir.
   * Playlist durumunda, listedeki her bir videonun boyutu arka planda tek tek taranarak liste elemanlarının yanında gösterilir.
3. **İndirme ve Durum Kontrolü:**
   * Kullanıcı "İndir" butonuna tıklar. Canlı ilerleme çubuğu (progress bar), indirme hızı (MB/s) ve kalan tahmini süre güncellenir.
   * İstendiğinde indirme işlemi duraklatılabilir (Pause), devam ettirilebilir (Resume) veya tamamen iptal edilebilir (Stop).

---

## ✨ Kullanıcı Deneyimi (UX) Kuralları (UX Guardrails)

* **Zengin ve Modern Estetik (Rich Aesthetics):** Koyu arka plan (`#131313`) üzerinde mor, mavi ve gri tonlarının kullanıldığı, yuvarlatılmış köşeler (rounded corners) ve yumuşak geçişlerin olduğu premium bir tasarım korunmalıdır.
* **Görsel Geri Bildirim (Visual Feedback):** Butonların üzerine gelindiğinde (hover) belirgin geçiş efektleri olmalıdır. İndirme durumu başarıyla tamamlandığında yeşil renkte net bir başarı bildirimi gösterilmelidir.
* **Arka Plan Akıcılığı (Smooth Operations):** Analiz ve indirme işlemleri sırasında UI hiçbir şekilde donmamalı, işlemler arka planda (daemon thread) yürütülmelidir.
* **Eksiksiz Bilgi Sunumu (Transparency):** Boyut hesaplanırken veya indirme yapılırken kullanıcı her aşamada bilgilendirilmeli, hata durumunda teknik kodlar yerine anlaşılır uyarı mesajları sunulmalıdır.
