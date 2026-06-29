Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
strPath = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Çalışma dizinini ayarla (dosya yolları ve kütüphane importları için kritik)
WshShell.CurrentDirectory = strPath

' Python dosyasının tam yolunu tırnaklar içine alarak oluşturuyoruz
pyScript = """" & strPath & "\indirici.py"""

On Error Resume Next

' Önce sistemde daha yaygın ve çalışan pythonw ile dene
Err.Clear
WshShell.Run "pythonw " & pyScript, 1, False

' Eğer pythonw hata verdiyse pyw ile dene
If Err.Number <> 0 Then
    Err.Clear
    WshShell.Run "pyw " & pyScript, 1, False
End If

' İkisi de tamamen başarısız olursa kullanıcıyı bilgilendir
If Err.Number <> 0 Then
    MsgBox "HATA: Python (pythonw veya pyw) bulunamadi!" & vbCrLf & "Lutfen Python'un kurulu ve PATH değişkenine ekli oldugundan emin olun.", 16, "YT Indirici Baslatici"
End If


