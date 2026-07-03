# 📜 Changelog — Vibe Coding Şablonu

> Şablonun sürüm geçmişi. Mevcut sürüm: `VERSION` dosyasında.
> Detaylı geliştirme tarihçesi: `memory-bank/archive/2026-sablon-tarihcesi.md`

---

## [2.0.0] — 2026-07-03

### 🔄 Değişti (Changed)
* **Editör-bağımsız kimlik:** "Antigravity IDE'desin, asla Cursor deme" dayatması kaldırıldı. Ajan artık hangi editörde çalışıyorsa (Cursor, Antigravity, Claude Code, Windsurf, Cline...) o editörün özelliklerine ve kısayollarına göre konuşur.
* **Temiz dağıtım hafızası:** `memory-bank/activeContext.md` ve `progress.md` şablonun kendi geçmişinden arındırıldı; yeni projeler tertemiz hafızayla başlar. Eski geçmiş `memory-bank/archive/2026-sablon-tarihcesi.md`'ye taşındı.
* **Köprü dosyaları inceltildi:** `.cursorrules`, `.clinerules`, `CLAUDE.md`, `GEMINI.md` sadece `AGENTS.md`'ye yönlendiren kısa köprüler haline getirildi (token tasarrufu — aynı kural artık 4 kopyada yüklenmiyor).
* **`upgrade_project.ps1` güvenli güncelleme:** Üzerine yazmadan önce hedef projedeki eski kural dosyalarını `.vibe-backup/<tarih>/` klasörüne yedekler; `VERSION` dosyasını da kopyalayarak projede hangi şablon sürümünün kurulu olduğunu izler.
* **Yol düzeltmeleri:** Eski `Desktop/vibecoding` konumuna işaret eden kırık dosya yolları ve var olmayan dosya atıfları temizlendi.
* `.cursorignore`'dan `*.svg` kaldırıldı (ikon dosyalarıyla çalışabilmek için).

### ➕ Eklendi (Added)
* `VERSION` — şablon sürüm numarası.
* `CHANGELOG.md` — bu dosya.
* `memory-bank/archive/` — eski oturum kayıtları için arşiv klasörü.

---

## [1.x] — 2026-06 ve öncesi (Özet)
* Memory Bank sistemi, modüler `.cursor/rules/` (100-400), çapraz editör köprüleri, MCP şablonları, token koruma kuralları (Mimar/İşçi handoff, minimal diff, 5 adım limiti), modern AI güvenlik kuralları (prompt injection / Lethal Trifecta), Fallow entegrasyonu, `upgrade_project.ps1` ve Türkçe dokümantasyon oluşturuldu.
