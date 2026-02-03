Add-Type -AssemblyName System.Windows.Forms
$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = 100
$timer.add_Tick({
    # التحقق من الضغط على Ctrl + Shift + A
    if ([System.Windows.Forms.Control]::ModifierKeys -eq 'Control, Shift' -and [System.Windows.Forms.Control]::IsKeyLocked([System.Windows.Forms.Keys]::A)) {
        # تشغيل واجهة الدردشة السيادية
        start-process pythonw.exe -ArgumentList "D:\Sovereign_System\Sovereign_Chat.py"
    }
})
$timer.Start()
[System.Windows.Forms.Application]::Run()
