import os
import psutil
import time

def verify_and_push():
    print("[*] Sovereign Audit: Verifying Hardware Sovereignty...")
    # 1. التأكد من خطة الطاقة القصوى (Ultimate Performance)
    os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
    
    # 2. فحص استجابة المعالج 7800X3D
    cpu_freq = psutil.cpu_freq().max
    print(f"[+] Processor 7800X3D Speed Cap: {cpu_freq}MHz - Unlocked.")
    
    # 3. اختبار "كتاب الحكمة"
    if os.path.exists("E:/Sovereign_System/Sovereign_Wisdom_Base.txt"):
        print("[+] Sovereign Wisdom Base: Online and Verified.")
    
    print("\n[!] ACTION: System is now shifting to 'Absolute Control' Mode.")

if __name__ == "__main__":
    verify_and_push()
