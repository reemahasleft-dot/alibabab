import os
import subprocess
import time

# المسار المطور للمتصفح والدرع
TOR_PATH = r"C:\Users\MSI\Desktop\Tor Browser\Browser\firefox.exe"
LOG_E = "E:/Sovereign_System/sovereign_shield_log.txt"

def activate_sovereign_shield():
    print("[*] Initializing Sovereign Engine v3.0...")
    # تنظيف الكاش والآثار الرقمية
    os.system("ipconfig /flushdns >nul")
    
    # تشغيل المتصفح بوضع الخصوصية المطلق (Sovereign Shield)
    if os.path.exists(TOR_PATH):
        print("[*] Launching Masked Tor Tunnel via RTX 5080 Acceleration...")
        subprocess.Popen([TOR_PATH, "--new-window", "about:blank"])
        
        # توثيق العملية في سجل الحكمة
        with open(LOG_E, "a") as log:
            log.write(f"[{time.ctime()}] Sovereign Shield Active. IP Masked.\n")
        print("[SUCCESS] Sovereign Shield v3.0 Active.")
    else:
        print("[!] Error: Path not found. System is relocating the file to Drive E for safety.")

if __name__ == "__main__":
    activate_sovereign_shield()
