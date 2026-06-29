<!-- last_updated: 2026-06-06 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] `index.html` dosyasının HTML, CSS ve JS olarak üç bağımsız modüle ayrılması.
* [x] `indirici.py` backend kodunun yeni modüler yapıya göre güncellenip doğrulanması.
* [x] `derle.bat` derleme betiğinin güncellenmesi ve başarıyla derlenmesi.
* [x] Fallow statik analizi ile modüler yapı kontrolü ve JS/CSS dosya ayrımının taranması.

---

## 🔄 Son Değişiklikler (Recent Changes)

* **Vibe Coding Yapılandırma Güncellemesi:**
  * Kullanıcının ilettiği yeni `vibecoding_yeni` klasöründeki güncel kural ve ayar dosyaları (kurallar, yoksayma listeleri, rehberler) proje kök dizinine başarıyla entegre edildi.
  * Güncelleme sonrasında geçici `vibecoding_yeni` klasörü silinerek çalışma alanı temizlendi.
  * YT İndirici projesinin özgün hafıza bankası (`memory-bank`) verileri korunarak şablon dosyalar tarafından ezilmesi engellendi.
* **Arayüz Modülerizasyonu (Monolith Dosyanın Bölünmesi):**
  * `index.html` dosyasındaki CSS kodları `index.css` dosyasına taşındı.
  * `index.html` dosyasındaki JS kodları `index.js` dosyasına taşındı.
  * `index.html` içerisine CSS ve JS için sırasıyla `<!-- STYLESHEET_PLACEHOLDER -->` ve `<!-- SCRIPT_PLACEHOLDER -->` yer tutucuları yerleştirildi.
* **Dinamik Entegrasyon Mantığı:**
  * `indirici.py` üzerinde, PyInstaller ve WebView2 motorunun local file URI kısıtlamalarını aşmak amacıyla stil ve mantık dosyalarını çalışma zamanında `index.html` içerisine enjekte eden inlining mekanizması kuruldu.
* **Derleme Yapılandırması:**
  * `derle.bat` dosyası güncellenerek PyInstaller parametrelerine (`--add-data`) `index.css` ve `index.js` dosyaları dahil edildi. Derleme başarıyla tamamlandı.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: Arayüz Ayrıştırması ve Runtime Inlining:**
  * WebView2'nin relative file URI kısıtlamalarını aşmak için şablon yer tutucuları ve python inlining yaklaşımı benimsenmiştir. Bu, geliştirme aşamasında modülerliği korurken çalışma zamanı kararlılığını garanti eder.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] Kullanıcı tarafından uygulamanın yerel çalışma (`baslat.bat`) ve derlenmiş EXE (`indirici.exe`) testlerinin manuel olarak doğrulanması.
* [ ] Fallow'un tespit ettiği JS tekrarlarının (`dup:ded2a373`, `dup:3ebeb150`, `dup:40e52757`) temizlenmesi/refaktör edilmesi.
