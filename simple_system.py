# 🏃 بديل سريع إذا كان النظام الرئيسي لا يعمل
import os, time, psutil
from datetime import datetime

print("⚡ النظام السيادي المبسط - يعمل!")
print("="*50)

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    print(f"🖥️ CPU: {cpu}% | 💾 RAM: {ram}% | ⏰ {datetime.now().strftime('%H:%M:%S')}")
    time.sleep(3)
