@echo off
title YT Indirici Baslatici

:: Önce pyw.exe sistemde var mı diye kontrol et (böylece Windows hata uyarısı vermez)
where pyw >nul 2>&1
if %errorlevel% equ 0 (
    start "" pyw "%~dp0indirici.py"
    exit
)

:: pyw yoksa pythonw.exe var mı kontrol et ve çalıştır
where pythonw >nul 2>&1
if %errorlevel% equ 0 (
    start "" pythonw "%~dp0indirici.py"
    exit
)

:: İkisi de yoksa kullanıcıya hata göster
echo.
echo HATA: Python (pyw veya pythonw) sistemde bulunamadi!
echo Lutfen Python'un kurulu ve PATH ortam degiskenine ekli oldugundan emin olun.
pause


