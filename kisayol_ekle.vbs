Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
strPath = objFSO.GetParentFolderName(WScript.ScriptFullName)
strPrograms = WshShell.SpecialFolders("Programs")

' 1. YT Indirici
Set oShortcut1 = WshShell.CreateShortcut(strPrograms & "\YT Indirici.lnk")
oShortcut1.TargetPath = "wscript.exe"
oShortcut1.Arguments = """" & strPath & "\baslat.vbs"""
oShortcut1.WorkingDirectory = strPath
oShortcut1.IconLocation = strPath & "\logo.ico, 0"
oShortcut1.Description = "YouTube ve Sosyal Medya Video İndirici"
oShortcut1.Save

' 2. yt-indirici (Arama uyumluluğu için)
Set oShortcut2 = WshShell.CreateShortcut(strPrograms & "\yt-indirici.lnk")
oShortcut2.TargetPath = "wscript.exe"
oShortcut2.Arguments = """" & strPath & "\baslat.vbs"""
oShortcut2.WorkingDirectory = strPath
oShortcut2.IconLocation = strPath & "\logo.ico, 0"
oShortcut2.Description = "YouTube ve Sosyal Medya Video İndirici"
oShortcut2.Save

WScript.Echo "Başlat menüsü kısayolu başarıyla oluşturuldu!"

