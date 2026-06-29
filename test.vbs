Set WshShell = CreateObject("WScript.Shell")
strPath = "c:\Users\Admin\Desktop\yt-indirici"
WshShell.CurrentDirectory = strPath
WshShell.Run "pyw -3.12 """ & strPath & "\indirici.py""", 1, False
