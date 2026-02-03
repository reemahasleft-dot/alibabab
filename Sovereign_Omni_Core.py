import os
import shutil
import subprocess
import requests
import time

# تعريف المسارات السيادية
DRIVE_D = "D:/Sovereign_Project"
DRIVE_E = "E:/Sovereign_System"
LOG_PATH = "E:/Sovereign_System/history_log.txt"

def check_and_update_libraries():
    # الصلاحية الكاملة لتحديث المكتبات هندسياً
    libraries = ["watchdog", "requests", "numpy", "pandas"]
    print("[*] Checking for the latest 2026 engineering libraries...")
    for lib in libraries:
        subprocess.run(["pip", "install", "--upgrade", lib], capture_output=True)

def migrate_data():
    # حماية القرص D وترحيل البيانات للقرص E
    if os.path.exists(DRIVE_D):
        print(f"[*] Optimizing Drive D... Moving files to Drive E to preserve space.")
        for item in os.listdir(DRIVE_D):
            s = os.path.join(DRIVE_D, item)
            d = os.path.join(DRIVE_E, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
                shutil.rmtree(s)
            else:
                shutil.move(s, d)

def autonomous_loop():
    check_and_update_libraries()
    migrate_data()
    print("[+] System is now fully autonomous and updated.")

if __name__ == "__main__":
    autonomous_loop()
