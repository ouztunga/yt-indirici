# 🔍 Kod İnceleme (Code Review)

Projedeki kod kalitesini, modülerliği ve performansı incele.

## Adımlar

1. **Dosya Boyut Kontrolü:** 500 satırı aşan kaynak dosyalarını tespit et ve bölme önerisi sun.

2. **Ölü Kod Tespiti:** Kullanılmayan import'ları, fonksiyonları ve değişkenleri bul. (Fallow CLI kuruluysa `fallow analyze` komutunu kullan.)

3. **Tekrar Kod Tespiti:** Birbirine çok benzeyen kod blokları veya kopyala-yapıştır edilmiş fonksiyonları tespit et.

4. **Erişilebilirlik (a11y):** HTML elementlerinde `alt`, `aria-label`, `role` eksikliklerini kontrol et.

5. **Performans:** Gereksiz re-render, büyük bundle import'ları, optimize edilmemiş görselleri tespit et.

6. **Rapor:** Bulgularını Türkçe olarak önem sırasına göre listele. Her bulgu için dosya adı, satır numarası ve düzeltme önerisi yaz.
