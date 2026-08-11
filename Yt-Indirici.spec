# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas_clr, binaries_clr, hiddenimports_clr = collect_all('clr_loader')
datas_pn, binaries_pn, hiddenimports_pn = collect_all('pythonnet')
datas_wv, binaries_wv, hiddenimports_wv = collect_all('webview')

a = Analysis(
    ['indirici.py'],
    pathex=[],
    binaries=binaries_clr + binaries_pn + binaries_wv,
    datas=[
        ('index.html', '.'),
        ('index.css', '.'),
        ('index.js', '.'),
        ('logo.png', '.'),
        ('logo.ico', '.'),
        ('ffmpeg.exe', '.')
    ] + datas_clr + datas_pn + datas_wv,
    hiddenimports=[
        'yt_dlp',
        'yt_dlp.utils',
        'yt_dlp.extractor',
        'webview',
        'pywebview',
        'clr',
        'clr_loader',
        'pythonnet',
        'webview.platforms.edgechromium',
        'webview.platforms.winforms',
        'System.Windows.Forms',
        'Microsoft.Web.WebView2.WinForms',
        'Microsoft.Web.WebView2.Core'
    ] + hiddenimports_clr + hiddenimports_pn + hiddenimports_wv,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='indirici',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.ico'],
)
