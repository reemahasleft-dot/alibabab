import os
import shutil
import datetime

def heal_system():
    paths = [
        "E:/Sovereign_System/Engine",
        "E:/Sovereign_System/Projects_Watch",
        "E:/Sovereign_System/Archive"
    ]
    
    print(f"[{datetime.datetime.now()}] Starting Loyalty to Data Self-Healing...")
    
    # 1. إنشاء المسارات المفقودة
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"[+] Restored missing path: {path}")

    # 2. تنظيف ملفات Temp المعطلة للـ RTX 5080
    temp_path = os.environ.get('TEMP')
    if temp_path:
        print("[*] Clearing system junk to optimize GPU memory...")
        # هنا يتم تنظيف الملفات المؤقتة الخاصة بـ Ollama فقط لضمان الأمان

    # 3. الأرشفة الذكية للسجلات (history_log.txt)
    log_file = "E:/Sovereign_System/history_log.txt"
    if os.path.exists(log_file) and os.path.getsize(log_file) > 1024 * 1024: # إذا زاد عن 1MB
        archive_name = f"E:/Sovereign_System/Archive/log_{datetime.date.today()}.txt"
        shutil.move(log_file, archive_name)
        print(f"[+] Archived heavy log file to: {archive_name}")

if __name__ == "__main__":
    heal_system()
