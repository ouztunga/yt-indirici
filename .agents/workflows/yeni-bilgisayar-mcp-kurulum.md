# 🖥️ Yeni Bilgisayar — MCP Kurulum Prompt'u

> **Ne zaman kullan:** İş bilgisayarı, yeni PC veya format sonrası. Antigravity veya Cursor'da yeni sohbet aç, aşağıdaki metni **olduğu gibi** yapıştır.

---

## 📋 Kopyala-Yapıştır Prompt

```
Merhaba! Bu bilgisayarda vibe coding yapıyorum. Ev bilgisayarımda kurulu olan MCP süper güçlerini buraya da kurmanı istiyorum.

## Görevin
1. Önce bu projede veya açık klasörde `AGENTS.md` ve `mcp-config-template.json` var mı kontrol et (vibecoding şablonu). Varsa oku ve ona uy.
2. Aşağıdaki MCP sunucularını **küresel (global)** olarak kur — her yeni projede tekrar kurulmasın:
   - context7
   - playwright
   - sequential-thinking
   - fetch (uv kurulu değilse kurmayı dene veya fetch'i atla, kullanıcıya söyle)
   - github (resmî uzak sunucu)
   - brave-search EKLEME — gereksiz, editör zaten internete bağlanıyor

3. İki dosya oluştur veya güncelle:

   **Cursor (Windows):**
   `%USERPROFILE%\.cursor\mcp.json`
   - Uzak GitHub sunucusu için anahtar: `"url"` (Cursor formatı)

   **Antigravity 2.0 (Windows):**
   `%USERPROFILE%\.gemini\config\mcp_config.json`
   - Uzak GitHub sunucusu için anahtar: `"serverUrl"` (Antigravity formatı — `url` DEĞİL)
   - GitHub URL: https://api.githubcopilot.com/mcp/

4. GitHub token:
   - Benden token iste ama SOHBETE yazmamı isteme.
   - Token'ı sadece dosyaya yazacağım; sen placeholder bırak: `BURAYA_GITHUB_TOKEN_YAPIŞTIR`
   - Dosyaları oluşturduktan sonra bana hangi dosyayı açıp token yapıştıracağımı söyle.

5. Kurulum bitince bana Türkçe özet ver:
   - Hangi dosyalar oluşturuldu
   - Cursor: Settings → Tools & MCP → Refresh
   - Antigravity: Settings → Customizations → Installed MCP Servers → Refresh
   - Playwright'ı sadece ben söyleyince kullan (AGENTS.md kuralı)

6. Token'lı dosyaları git'e commit etme. `.gitignore`'a ekleme önerisi verme — zaten kullanıcı klasöründe.

## Referans — Cursor mcp.json örneği
{
  "mcpServers": {
    "context7": { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "playwright": { "command": "npx", "args": ["-y", "@playwright/mcp@latest"] },
    "sequential-thinking": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"] },
    "fetch": { "command": "uvx", "args": ["mcp-server-fetch"] },
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer BURAYA_GITHUB_TOKEN_YAPIŞTIR" }
    }
  }
}

## Referans — Antigravity mcp_config.json örneği
{
  "mcpServers": {
    "context7": { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "playwright": { "command": "npx", "args": ["-y", "@playwright/mcp@latest"] },
    "sequential-thinking": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"] },
    "fetch": { "command": "uvx", "args": ["mcp-server-fetch"] },
    "github": {
      "serverUrl": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer BURAYA_GITHUB_TOKEN_YAPIŞTIR" }
    }
  }
}

Onay bekleme — bu kurulum görevi, direkt dosyaları oluştur ve bana ne yapmam gerektiğini söyle.
```

---

## 🔐 Token sonrası (sen yap)

1. Ajan dosyaları oluşturduktan sonra sana yol verecek.
2. `BURAYA_GITHUB_TOKEN_YAPIŞTIR` yerine GitHub token'ını **dosyada** yapıştır (sohbete değil).
3. Cursor + Antigravity → **Refresh**
4. Yeşil görünüyorsa hazır.

## 🆕 Yeni proje başlatma (MCP sonrası)

```
Bellek bankasını oku ve projemizi başlatalım.
```

Ajan MCP brifingini de verecek (AGENTS.md kuralı).
