# Claude Code Playbook

> **Evrensel kurallar için:** Proje kökündeki `AGENTS.md` dosyasını okuyun.
> Bu dosya YALNIZCA Claude Code'a özgü ek bilgileri içerir.
> Hiyerarşi: `~/.claude/CLAUDE.md` (global) → `./CLAUDE.md` (proje) → `./.claude/rules/` (kapsamlı)

---

## Claude Code'a Özel Bilgiler

### Slash Commands
* `/fallow` — Fallow codebase intelligence analizi başlatır (`.claude/commands/fallow.md`)

### Skills
* `.claude/skills/fallow/` — Fallow CLI entegrasyonu

### Compact Mode
* Büyük dosya düzenlemelerinde Claude Code'un `compact` modunu tercih et.
* Diff çıktılarında sadece değişen satırları göster.

### Tool Use
* `TodoWrite` ile görev takibi yap — `task.md` yerine Claude'un kendi todo sistemini kullanabilirsin.
* `bash` tool'u ile terminal komutlarını çalıştır, sonuçları 50 satırla sınırla.
