import os
import shutil
import pyttsx3

engine = pyttsx3.init()

def sovereign_cleanse():
    print("[🛡️] Immunity Shield: Initiating System Cleansing...")
    # تنظيف مجلدات Temp لضمان سرعة Blackwell
    temp_folders = [os.environ.get('TEMP'), r'C:\Windows\Temp']
    for folder in temp_folders:
        try:
            shutil.rmtree(folder, ignore_errors=True)
            print(f"[+] Cleansed: {folder}")
        except: pass
    
    engine.say("System immunity protocols applied. Performance is pure.")
    engine.runAndWait()

if __name__ == "__main__":
    sovereign_cleanse()
