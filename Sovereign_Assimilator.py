import os
import shutil

# مسارات الأدوات القديمة التي سيتم هضمها
LEGACY_PATHS = ["D:/Sovereign_System", "E:/Sovereign_System/Migrated_Legacy"]
SOVEREIGN_CORE = "E:/Sovereign_System/Core_Intelligence"

def assimilate_tools():
    print("[*] Sovereign Assimilator: Starting Universal Ingestion...")
    if not os.path.exists(SOVEREIGN_CORE):
        os.makedirs(SOVEREIGN_CORE)

    for path in LEGACY_PATHS:
        if os.path.exists(path):
            print(f"[*] Digesting tools in: {path}")
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(('.py', '.bat', '.ps1')):
                        # قراءة المنطق وتحليله (الهضم)
                        print(f"[+] Assimilating Logic from: {file}")
                        # نقل الأداة لتكون تحت سلطة النواة المركزية
                        shutil.move(os.path.join(root, file), os.path.join(SOVEREIGN_CORE, file))
    
    print("[SUCCESS] All legacy tools have been digested into the Sovereign Core.")

if __name__ == "__main__":
    assimilate_tools()
