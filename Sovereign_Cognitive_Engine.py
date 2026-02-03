import psutil
import time
import ctypes
import os

# بروتوكول تحسين الأداء المطلق
def boost_system_for_action(process_name):
    print(f"[*] Detected Action: {process_name}. Reconfiguring Blackwell Cores...")
    # رفع أولوية المعالجة لأقصى درجة (Realtime Priority)
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            try:
                proc.nice(psutil.REALTIME_PRIORITY_CLASS)
                print(f"[+] {process_name} is now Sovereign Priority.")
            except: pass

def active_memory_management():
    # تنظيف الذاكرة بشكل لا يؤثر على الأداء (Silent Purge)
    threshold = 75.0
    if psutil.virtual_memory().percent > threshold:
        ctypes.windll.psapi.EmptyWorkingSet(ctypes.windll.kernel32.GetCurrentProcess())

if __name__ == "__main__":
    print("--- Sovereign Cognitive Engine Active ---")
    while True:
        # رصد تلقائي لأي برنامج "معماري" أو "لعبة"
        targets = ["Cyberpunk2077.exe", "Revit.exe", "chrome.exe", "msedge.exe"]
        for target in targets:
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == target:
                    boost_system_for_action(target)
        active_memory_management()
        time.sleep(5)
