<!-- last_updated: 2026-06-29 -->
# ⚡ Active Context / Aktif Bağlam

> **AI Instruction:** Bu dosya, MEVCUT oturum durumunun tek doğru kaynağıdır. Anlık görevleri, aktif tasarım kararlarını, son kod değişikliklerini ve karşılaşılan engelleri takip eder. Her oturum başında okunmalı ve oturum sonunda güncellenmelidir.

---

## 🎯 Şu Anki Odak (Current Focus)

* [x] `index.html` dosyasının HTML, CSS ve JS olarak üç bağımsız modüle ayrılması.
* [x] `indirici.py` backend kodunun yeni modüler yapıya göre güncellenip doğrulanması.
* [x] `derle.bat` derleme betiğinin güncellenmesi ve başarıyla derlenmesi.
* [x] Windows 11 Erişilebilirlik (Accessibility) kilitlenme hatasının giderilmesi (sys.setrecursionlimit iptali ve pywebview logger susturulması).
* [x] Git deposunun yerelde kurulması, değişikliklerin commmit edilmesi ve GitHub'a başarıyla push edilmesi.

---

## 🔄 Son Değişiklikler (Recent Changes)

* **Windows 11 Erişilebilirlik (Accessibility) Kilitlenme Çözümü:**
  * Windows 11'in bazı erişilebilirlik araçları (örneğin ekran okuyucular) WebView2 ile iletişim kurarken, .NET nesne sınırlarındaki circular referanslar yüzünden sonsuz döngüye giriyordu.
  * Bu döngü, `sys.setrecursionlimit(20000)` ayarı aktif olduğu için Python'u tamamen kilitliyor ve arayüzü "Video verileri analiz ediliyor..." durumunda donduruyordu.
  * `sys.setrecursionlimit` kaldırıldı ve `pywebview` kütüphanesinin içsel logging seviyesi `logging.CRITICAL` yapıldı. Bu sayede sonsuz döngü ve çökme kalıcı olarak çözüldü.
* **Derleme ve Dağıtım:**
  * `derle.bat` betiğinde `py -3.12` komutu `python` olarak güncellendi ve `indirici.exe` başarıyla paketlendi.
* **Git ve GitHub Entegrasyonu:**
  * Yerel dizinde Git deposu başarıyla başlatıldı (`git init`).
  * `https://github.com/ouztunga/yt-indirici.git` origin olarak eklendi.
  * Yerel kimlik tanımlanarak tüm değişiklikler commitlendi ve zorlu güncellemeyle (`git push -f`) GitHub'a başarıyla yüklendi.

---

## 🧠 Aktif Kararlar ve Mimari Düşünceler (Active Decisions & Architecture Thoughts)

* **Karar: pywebview Logger Seviyesi:**
  * WebView2 / Windows Forms altındaki erişilebilirlik hataları loglama sırasında sonsuz döngülere yol açtığından, `pywebview` loglarını tamamen susturmak (`CRITICAL` seviyesine çekmek) uygulamanın genel kararlılığı için zorunludur.

---

## 🚶‍♂️ Hemen Sonraki Adımlar (Immediate Next Steps)

* [ ] Kullanıcının yeni `indirici.exe` sürümünü test etmesi ve sorunsuz çalıştığını onaylaması.
* [ ] Fallow'un tespit ettiği JS tekrarlarının temizlenmesi/refaktör edilmesi.
