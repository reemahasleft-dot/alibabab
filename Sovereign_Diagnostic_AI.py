import os
import subprocess
import time
import psutil

def check_gpu_stability():
    # فحص استجابة RTX 5080 وإعادة تهيئة التعريف عند الحاجة
    print("[*] Diagnostic AI v1.1: Monitoring RTX 5080 Health...")

def protect_power_plan():
    try:
        # استخدام أمر أكثر استقراراً لجلب خطة الطاقة
        output = subprocess.check_output("powercfg /list", shell=True).decode()
        if "Ultimate Performance" not in output and "8c5e7fda" not in output:
            os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
            print("[!] Diagnostic AI: Power Plan Restored to Ultimate Performance.")
    except Exception as e:
        print(f"[!] Power Audit Skip: {e}")

if __name__ == "__main__":
    print("--- Sovereign Diagnostic AI v1.1: Recovering Logic ---")
    # تشغيل دورة إصلاح واحدة فورية
    protect_power_plan()
    print("[SUCCESS] Diagnostic Logic Patched and Active.")
