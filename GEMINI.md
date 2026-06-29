# Gemini CLI & Gemini Code Assist Playbook

> **Evrensel kurallar için:** Proje kökündeki `AGENTS.md` dosyasını okuyun.
> Bu dosya YALNIZCA Gemini'ye özgü ek bilgileri içerir.

---

## Gemini'ye Özel Bilgiler

### Model Routing
* Planlama ve mimari: Gemini Pro veya Claude Opus (thinking modu açık)
* Kodlama ve execution: Gemini Flash veya Claude Sonnet (hızlı ve ucuz)

### Bağlam Yönetimi
* Gemini'nin bağlam penceresi geniş olsa da, gereksiz dosya okumaları token harcar.
* Her zaman `grep` veya satır-aralığı okuma kullan, tüm dosyayı okumaktan kaçın.

### Agentic Mode
* Gemini CLI'da `--sandbox` flag'i ile güvenli ortamda çalıştır.
* Uzun görevlerde otomatik checkpoint commit'leri öner.
