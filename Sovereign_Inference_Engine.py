import psutil
import os
import time

# البرامج المستهدفة للارتقاء المعماري
ARCH_APPS = ["Revit.exe", "acad.exe", "3dsmax.exe", "Lumion.exe"]

def sovereign_inference_loop():
    print("[*] Sovereign Eye: Monitoring Engineering Environments...")
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] in ARCH_APPS:
                # 1. تخصيص موارد Blackwell الفائقة
                print(f"[+] Architect Ali Detected: Optimizing RTX 5080 for {proc.info['name']}")
                os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
                
                # 2. رفع أولوية الوصول للذاكرة (I/O Priority) لضمان سلاسة التنقل في الموديل
                try:
                    proc.nice(psutil.HIGH_PRIORITY_CLASS)
                except: pass
                
        time.sleep(10) # فحص هادئ كل 10 ثواني لضمان السيادة

if __name__ == "__main__":
    sovereign_inference_loop()
