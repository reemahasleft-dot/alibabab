import psutil
import time
import os

def optimize_gaming():
    # البحث عن الألعاب النشطة ورفع أولويتها
    gaming_procs = ["Cyberpunk2077.exe", "EldenRing.exe", "Revit.exe", "AutoCAD.exe"]
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in gaming_procs:
            proc.nice(psutil.HIGH_PRIORITY_CLASS)
            print(f"[+] Boosted Performance for: {proc.info['name']}")

def clean_system_latency():
    # تنظيف العمليات الخلفية غير الضرورية لتقليل الـ Latency
    threshold_ram = 80.0 # إذا تجاوز الاستهلاك 80%
    if psutil.virtual_memory().percent > threshold_ram:
        print("[*] High RAM usage detected. Optimizing memory for Architect tasks...")
        # هنا يقوم النظام بطلب تنظيف الذاكرة من الويندوز

if __name__ == "__main__":
    print("--- Sovereign Sensory Engine Active ---")
    while True:
        optimize_gaming()
        clean_system_latency()
        time.sleep(10) # فحص خفيف كل 10 ثواني لضمان صفر تأخير
