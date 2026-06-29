# 🔮 Ultimate Vibe Coding Başlangıç Şablonu

Bu klasör, kodlama bilgisine ihtiyaç duymadan sadece yapay zeka ajanlarını (Cursor, Windsurf, Claude Code, Cline vb.) kullanarak harika uygulamalar, oyunlar ve programlar geliştirmeniz için özel olarak yapılandırılmış **"Son Teknoloji Yapay Zeka Bellek Bankası ve Kural Sistemidir"**.

Yapay zekanın en büyük zayıflığı olan **"sohbet ilerledikçe eskiyi unutma"** ve **"saçmalama/hata yapma"** sorunlarını tamamen çözer. Ajanınız her başladığında projenizi mükemmel hatırlar, güncel kalır ve sizinle kusursuz bir uyumla çalışır.

---

## 📂 Şablon Klasör Yapısı

*   📁 `.cursor/rules/` ➜ Yapay zekaya kod yazma sınırları koyan, saçmalamasını engelleyen en yeni **Modüler Kurallar** (`100-vibe-core.mdc`, `200-tech-stack.mdc`, `300-planning.mdc`).
*   📁 `memory-bank/` ➜ Yapay zekanın **"Uzun Vadeli Belleği"**. Projenizin amacını, kurallarını, nereye varacağını ve o an ne yapıldığını içeren markdown dosyaları.
*   📄 `mcp-config-template.json` ➜ Yapay zekaya internette arama, tarayıcı yönetme, dosya okuma/yazma gibi **süper güçler** veren Model Context Protocol ayar şablonu.
*   📄 `.cursorrules`, `.clinerules`, `ANTIGRAVITY.md`, `CLAUDE.md` ➜ Farklı AI programları (Antigravity 2.0, Claude Code, Windsurf, Cline vb.) kullandığınızda şablonun aynı kalitede çalışmasını sağlayan çapraz uyumluluk dosyaları.

---

## 🚀 Yeni Bir Projeye Nasıl Başlanır? (Adım Adım)

1.  **Şablonu Kopyalayın:** Yeni ve bomboş bir klasör oluşturun (Örn: `benim-yeni-oyunum`). Bu şablon klasörünün içindeki tüm dosyaları (gizli `.cursor` klasörü dahil) o boş klasöre yapıştırın.
2.  **Editörünüzde Açın:** Klasörü **Cursor** veya **Windsurf** gibi bir yapay zeka editöründe açın.
3.  **Hafızayı Başlatın:** Yapay zeka sohbet panelini açın ve sadece şunu yazın:
    > **"Bellek bankasını oku ve projemizi başlatalım."**
4.  **Fikrinizi Söyleyin:** Yapay zeka size projenin ne olduğunu soracaktır. Fikrinizi Türkçe ve basitçe anlatın:
    > *"Ben çocuklara çarpım tablosunu öğreten, rengarenk, balon patlatmalı bir web oyunu yapmak istiyorum. Çok modern görünsün ve animasyonlu olsun."*
5.  **Planı Onaylayın:** Kurallarımız gereği yapay zeka doğrudan koda dalmayacak, önce size Türkçe bir plan sunacaktır. Planı okuyup **"Onaylıyorum, devam et"** dediğinizde kodları kendi kendine yazmaya başlayacaktır!

---

## 🧠 Bellek Bankası (Memory Bank) Nedir?

Yapay zeka modellerinin belleği sınırlıdır; sohbet uzadıkça 10 adım önce ne konuştuğunuzu unuturlar. Bu şablon, yapay zekanın her şeyi sabit dosyalara yazarak hatırlamasını sağlar.

*   `projectbrief.md`: Projenin genel amacı ve ana hedefleri.
*   `productContext.md`: Kullanıcı deneyimi, ekranların nasıl görüneceği ve uygulamanın "vibe"ı.
*   `systemPatterns.md`: Kod mimarisi, dosya yapısı ve klasörleme kuralları.
*   `techContext.md`: Hangi teknolojilerin kullanıldığı ve projeyi çalıştırma komutları.
*   `activeContext.md`: **[En Önemlisi]** O sohbet oturumunda ne yapıldığı ve bir sonraki adımın ne olduğu.
*   `progress.md`: Tamamlanan işler, yapılacaklar listesi (TODO) ve bilinen hatalar.

> [!TIP]
> **Yapay Zeka Hafızasını Kaybederse Ne Yapmalısınız?**
> Yeni bir sohbete başladığınızda veya yapay zeka şaşırdığında sadece şunu yazın:
> **"Bellek bankasını (memory bank) oku ve nerede kaldığımıza bak."**
> Ajanınız anında eski güncelliğine kavuşacaktır.

---

## 🛠️ MCP (Model Context Protocol) Süper Güçleri

MCP, yapay zekanın bilgisayarınızla ve internetle doğrudan iletişim kurmasını sağlayan sihirli bir köprüdür. 

### Nasıl Kurulur? (Cursor İçin)
1.  Klasörünüzdeki `mcp-config-template.json` dosyasını açın.
2.  Cursor ayarlarınızı açın: **Settings ➜ Features ➜ MCP** sekmesine gidin.
3.  Orada yeni bir MCP ekleme butonu göreceksiniz. `command` kısmına `npx` ve ilgili argümanları girerek `filesystem` (dosya erişimi) veya `fetch` (doküman okuma) MCP'lerini kolayca tanımlayabilirsiniz.
4.  Bu sayede yapay zeka bilgisayarınızdaki dosyalara erişebilir, hataları kendisi okuyup kendisi düzeltebilir!

---

## 💸 Akıllı Token ve Bütçe Koruması (Token & Cost Protection)

Ajanların kontrolsüz token tüketmesini ve bütçenizi tüketmesini engellemek için bu şablon **"Altın Standart"** token tasarrufu kurallarıyla donatılmıştır:

1.  **Mimar/İşçi Ayrımı (Planner/Worker split):** Planlamayı en akıllı modele yaptırıp, kodlama işini ucuz ve hızlı olan modellere (Gemini Flash, Claude Sonnet vb.) devrederek performansı düşürmeden devasa tasarruf sağlarsınız.
2.  **Sohbet Sıfırlama Alışkanlığı (/clear):** Ajan geçmişteki tüm mesajları ve dosyaları tekrar tekrar okumasın diye, 10-15 adımdan sonra size sohbeti temizleme uyarısı ve kopyalanabilir bir durum özeti verilecektir.
3.  **Yoksayma Dosyaları (.clineignore & .cursorignore):** Ağır medya, derleme (build) ve kütüphane dosyaları taranmaz, böylece bağlam penceresi gereksiz şişmez.
4.  **Minimal Kod Güncellemeleri:** Ajan tüm kod dosyasını baştan yazmak yerine sadece değişmesi gereken satırları (minimal diff) günceller.
5.  **Log Sıkıştırma ve Döngü Kırıcı:** Hata loglarının sadece en önemli kısımları okunur ve otonom döngülerde 5 adımdan sonra durup sizden onay istenir.

---

## 🤝 Kusursuz Vibe Coding İçin İletişim İpuçları

Yapay zekanın en yüksek kalitede çalışmasını sağlamak için sohbet ederken şu kalıpları kullanabilirsiniz:

*   **Plan Yaptırmak İçin:** *"Şimdi şu özelliği eklemek istiyorum. Önce planı hazırlayıp bana sun, onaylayınca kodlamaya geç."*
*   **Büyük Hatalarda:** Yapay zeka bir hata verip bunu döngüsel olarak çözemezse sohbeti kesin ve şunu yazın:
    > *"Şu an bir kısır döngüye girdin. Dur, `activeContext.md` dosyasını oku ve hata yaptığımız yeri baştan analiz et."*
*   **Tasarımı Güzelleştirmek İçin:** *"Bu sayfa çok sade ve basit duruyor. Ona biraz HSL renk paleti, yumuşak gölgeler, buton hover efektleri ve cam efekti (glassmorphism) ekleyerek premium hissettir."*
*   **Paket Uyarısı:** Yapay zeka bazen hatayı çözmek için bilgisayarınıza gereksiz 10 tane kütüphane indirmeye çalışır. Kurallarımız bunu engeller ama siz de uyarabilirsiniz:
    > *"Harici paket indirme, saf kod (pure code) veya kendi yazdığın küçük fonksiyonlarla çözmeye çalış."*

---

## 🚀 Artık Vibe Coding Başlamaya Hazır!
Bu klasörü kopyalayın, fikirlerinizi yapay zekaya söyleyin ve sadece izleyin! Yazılım geliştirmek hiç bu kadar keyifli olmamıştı. ✨
