@echo off
title YT Indirici Derleyici
echo EXE olusturuluyor, lutfen bekleyin...

:: Eski build klasörlerini temizle
if exist build rd /s /q build
if exist dist rd /s /q dist

:: PyInstaller ile spec dosyasından derle
python -m PyInstaller --noconfirm Yt-Indirici.spec

if %errorlevel% equ 0 (
    echo.
    echo BASARILI: Yt-Indirici.exe 'dist' klasorunde olusturuldu.
    echo Ana klasore kopyalaniyor...
    copy /y dist\Yt-Indirici.exe .
    copy /y dist\Yt-Indirici.exe indirici.exe
    echo Islem tamamlandi!
) else (
    echo.
    echo HATA: Derleme sirasinda bir sorun olustu.
)

