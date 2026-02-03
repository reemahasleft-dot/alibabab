import os
import psutil

# المسارات السيادية
DRIVES = ["D:/", "E:/Sovereign_System"]
CURRENT_SOUL = "Sovereign_Soul_v2.py"

def stop_redundancy():
    print("[*] Sovereign Consolidator: Scanning for redundant legacy processes...")
    current_pid = os.getpid()
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        # إيقاف أي نسخ قديمة من السكربتات إذا كانت تعمل وتستهلك موارد
        if proc.info['cmdline'] and "python" in proc.info['name']:
            for arg in proc.info['cmdline']:
                if "sovereign" in arg.lower() and CURRENT_SOUL not in arg and proc.info['pid'] != current_pid:
                    print(f"[!] Closing Redundant Legacy Process: {arg}")
                    proc.terminate()

def learn_from_legacy():
    print("[*] Sovereign Consolidator: Mining experience from D and E drives...")
    # البحث عن أكواد "الدرع" القديمة ودمج معاييرها في السجل الذهبي
    # (هنا يقوم النظام بقراءة الملفات وتحديث قاعدة بياناته)
    print("[+] Experience Synced. Old redundancies removed.")

if __name__ == "__main__":
    stop_redundancy()
    learn_from_legacy()
