# Gemini CLI & Code Assist Köprüsü

> **Tüm kurallar `AGENTS.md` dosyasındadır — önce onu oku.**
> Bu dosya YALNIZCA Gemini'ye özgü ek bilgileri içerir.

## Gemini'ye Özel
* **Model Handoff:** Plan Gemini Pro/thinking ile; plan sonunda "hızlı modele geç ve onay de" — kodlamayı Flash yapar (`AGENTS.md` → Mimar/İşçi).
* **Bağlam:** Geniş pencereye güvenme; grep / satır-aralığı okuma kullan, tüm dosyayı okuma.
* **Güvenlik:** Gemini CLI'da `--sandbox` ile çalıştır; uzun görevlerde checkpoint commit öner.
