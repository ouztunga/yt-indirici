@echo off
title YT Indirici Derleyici
echo EXE olusturuluyor, lutfen bekleyin...

:: Eski build klasörlerini temizle
if exist build rd /s /q build
if exist dist rd /s /q dist
if exist indirici.spec del /f /q indirici.spec

:: PyInstaller ile derle
python -m PyInstaller --noconfirm --onefile --windowed --icon "logo.ico" --add-data "index.html;." --add-data "index.css;." --add-data "index.js;." --add-data "logo.png;." --add-data "logo.ico;." --name "indirici" "indirici.py"

if %errorlevel% equ 0 (
    echo.
    echo BASARILI: indirici.exe 'dist' klasorunde olusturuldu.
    echo Ana klasore kopyalaniyor...
    copy /y dist\indirici.exe .
    echo Islem tamamlandi!
) else (
    echo.
    echo HATA: Derleme sirasinda bir sorun olustu.
)

pause
