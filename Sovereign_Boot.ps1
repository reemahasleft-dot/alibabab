# تأخير بسيط لضمان تحميل خدمات النظام
Start-Sleep -Seconds 10

# إصلاح الصوت فوراً باستخدام المسار الذي استخرجناه
$VMPATH = [Environment]::GetEnvironmentVariable("VM_SOVEREIGN_PATH", "User")
if ($VMPATH) { Start-Process $VMPATH -ArgumentList "-R" }

# تشغيل مركز القيادة (Omni-Control)
Start-Process pythonw.exe -ArgumentList "D:\Sovereign_System\Omni_Control.py"

# تحية المعماري وبدء العقل الثالث
$Message = "Architect Ali Essa, The Three Brains are now integrated. System is at Maximum Performance. Elysium Archives are secure."
Add-Type -AssemblyName System.Speech
$Synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$Synth.Speak($Message)
