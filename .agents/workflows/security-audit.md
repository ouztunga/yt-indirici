# 🔒 Güvenlik Taraması (Security Audit)

Projedeki güvenlik açıklarını tara ve raporla.

## Adımlar

1. **Hardcoded Secret Taraması:** Tüm kaynak dosyalarında (`src/`, `app/`, `pages/`) API key, token, password veya secret içeren satırları `grep` ile ara. Pattern'ler: `API_KEY`, `SECRET`, `PASSWORD`, `TOKEN`, `Bearer`, `sk-`, `pk_`.

2. **XSS Vektör Kontrolü:** `dangerouslySetInnerHTML`, `innerHTML`, `document.write`, `eval(` kullanımlarını ara.

3. **HTTP Kontrolü:** `http://` ile başlayan URL'leri ara (HTTPS zorunluluğu ihlali).

4. **Env Dosyası Kontrolü:** `.env` dosyalarının `.gitignore`'da listelenip listelenmediğini doğrula.

5. **Console.log Hassas Veri:** `console.log` içinde potansiyel hassas veri loglaması olup olmadığını kontrol et.

6. **Rapor:** Bulgularını Türkçe olarak önem sırasına göre (KRİTİK → UYARI → BİLGİ) listele ve düzeltme önerileri sun.
