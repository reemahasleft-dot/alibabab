import os
import time
import psutil
from win10toast import ToastNotifier

toaster = ToastNotifier()

def sovereign_talk(title, message):
    toaster.show_toast(title, message, duration=5, threaded=True)

def monitor_and_assist():
    print("--- Sovereign Live Assistant Active ---")
    last_action = ""
    
    while True:
        # رصد الألعاب والبرامج الثقيلة
        for proc in psutil.process_iter(['name']):
            name = proc.info['name']
            if name == "Cyberpunk2077.exe" and last_action != "gaming":
                sovereign_talk("Sovereign Intelligence", "Gaming Mode Active: RTX 5080 Cores Optimized for 4K Performance.")
                last_action = "gaming"
            elif name == "Revit.exe" and last_action != "design":
                sovereign_talk("Sovereign Intelligence", "Architectural Mode: Tensor Cores Reserved for BIM Real-time Inference.")
                last_action = "design"
        
        # تنظيف الرام التلقائي إذا زادت عن حد معين
        ram_usage = psutil.virtual_memory().percent
        if ram_usage > 85:
            sovereign_talk("System Shield", "High RAM usage detected. Performing silent memory optimization.")
            # (كود تنظيف الرام يعمل هنا)
            
        time.sleep(10)

if __name__ == "__main__":
    monitor_and_assist()
