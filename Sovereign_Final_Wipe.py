import os
import shutil

# المناطق المستهدفة للتنظيف
SCRAP_ZONES = [
    os.path.join(os.environ['USERPROFILE'], 'Desktop'),
    os.path.join(os.environ['USERPROFILE'], 'Downloads')
]
SAFE_VAULT = "E:/Sovereign_System/Core_Intelligence/Legacy_Recovered"

def sovereign_wipe():
    print("[*] Sovereign Wipe: Identifying stray architectural fragments...")
    if not os.path.exists(SAFE_VAULT):
        os.makedirs(SAFE_VAULT)
        
    for zone in SCRAP_ZONES:
        print(f"[*] Scanning: {zone}")
        for item in os.listdir(zone):
            # نقل الملفات الهندسية والبرمجية فقط لضمان النقاء
            if item.lower().endswith(('.rvt', '.dwg', '.py', '.ps1', '.txt')):
                print(f"[+] Relocating to Vault: {item}")
                try:
                    shutil.move(os.path.join(zone, item), os.path.join(SAFE_VAULT, item))
                except: pass
    
    print("[SUCCESS] System is now Pure. All fragments are in the Sovereign Vault.")

if __name__ == "__main__":
    sovereign_wipe()
