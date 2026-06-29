# Memory Bank dosyalarına last_updated zaman damgası ekler.
# Kullanım: Bu scripti proje kök dizininden çalıştırın.

$mbPath = Join-Path $PSScriptRoot "memory-bank"
$date = (Get-Date).ToString("yyyy-MM-dd")
$files = @("projectbrief.md", "productContext.md", "systemPatterns.md", "techContext.md", "activeContext.md", "progress.md")

foreach ($file in $files) {
    $fullPath = Join-Path $mbPath $file
    if (Test-Path $fullPath) {
        $content = Get-Content $fullPath -Raw
        # Mevcut timestamp varsa güncelle, yoksa ekle
        if ($content -match '<!-- last_updated: .* -->') {
            $content = $content -replace '<!-- last_updated: .* -->', "<!-- last_updated: $date -->"
        } else {
            $content = "<!-- last_updated: $date -->`r`n" + $content
        }
        Set-Content -Path $fullPath -Value $content -NoNewline
        Write-Host "✅ Updated: $file"
    } else {
        Write-Host "⚠️ Not found: $file"
    }
}

Write-Host "`n✅ Done - all memory bank files updated with last_updated: $date"
