import os
import psutil
import threading
import pyttsx3
import time
import json
import shutil
import subprocess
import atexit
from datetime import datetime, timedelta
from pynvml import *

class SovereignOmnibusFinal:
    def __init__(self):
        self.architect = "Ali Essa"
        self.base_path = "E:/Sovereign_System"
        self.log_path = f"{self.base_path}/Logs"
        self.data_path = f"{self.base_path}/Data"
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
        # إنشاء البنية التحتية [cite: 2026-01-02]
        for path in [self.log_path, self.data_path]:
            if not os.path.exists(path): os.makedirs(path)

        # عتبات الانحراف الهندسي
        self.IDLE_UTIL_LIMIT = 20 
        self.IDLE_FAN_LIMIT = 65  
        self.IDLE_TEMP_LIMIT = 70 

        # تهيئة NVML وضمان الإغلاق النظيف
        try:
            nvmlInit()
            atexit.register(nvmlShutdown)
        except: pass

        # تفعيل المحركات العصبية (بما فيها حارس الصوت المستعاد)
        threading.Thread(target=self.thermal_drift_engine, daemon=True).start()
        threading.Thread(target=self.maintenance_advisory_engine, daemon=True).start()
        threading.Thread(target=self.dynamic_priority_governor, daemon=True).start()
        threading.Thread(target=self.audio_watchdog, daemon=True).start()
        threading.Thread(target=self.safe_purification, daemon=True).start()
        
        self.proclaim("Sovereign Phase 4.2 Certified. Audio Guardian restored. System is live.")

    def proclaim(self, text):
        print(f"[🔱] OMNIBUS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def audio_watchdog(self):
        """حارس الصوت: إعادة تشغيل Voicemeeter عند الانهيار [cite: 2026-01-04]"""
        vm_path = r"C:\Program Files (x86)\VB\Voicemeeter\voicemeeter8x64.exe"
        while True:
            vm_active = any("voicemeeter" in p.name().lower() for p in psutil.process_iter(['name']))
            if not vm_active and os.path.exists(vm_path):
                subprocess.Popen([vm_path])
                self.log_event("AUDIO_FIX", "Voicemeeter restarted by Guardian.")
            time.sleep(60)

    def thermal_drift_engine(self):
        """رصد الانحراف الحراري لـ RTX 5080 [cite: 2025-08-05]"""
        try:
            handle = nvmlDeviceGetHandleByIndex(0)
            while True:
                util = nvmlDeviceGetUtilizationRates(handle).gpu
                temp = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)
                fan = nvmlDeviceGetFanSpeed(handle)
                if util < self.IDLE_UTIL_LIMIT and fan > self.IDLE_FAN_LIMIT and temp > self.IDLE_TEMP_LIMIT:
                    self.log_drift_event(temp, fan, util)
                self.save_thermal_history(temp, fan, util)
                time.sleep(600)
        except: pass

    def log_drift_event(self, temp, fan, util):
        event = {"date": str(datetime.now().date()), "t": temp, "f": fan, "u": util}
        with open(f"{self.data_path}/drift_events.json", "a") as f:
            f.write(json.dumps(event) + "\n")

    def maintenance_advisory_engine(self):
        """الاستشارة الاستباقية بناءً على نمط 3 أيام"""
        while True:
            time.sleep(3600 * 12)
            if self.check_persistence(days=3):
                self.proclaim("Thermal drift persists. Recommended: air dust cleaning.")

    def check_persistence(self, days):
        if not os.path.exists(f"{self.data_path}/drift_events.json"): return False
        with open(f"{self.data_path}/drift_events.json", "r") as f:
            events = [json.loads(line) for line in f]
        last_days = [str((datetime.now() - timedelta(days=i)).date()) for i in range(days)]
        dates_in_log = {e['date'] for e in events}
        return all(d in dates_in_log for d in last_days)

    def dynamic_priority_governor(self):
        """إدارة الـ 7800X3D بفاصل زمني دقيق [cite: 2026-01-01]"""
        while True:
            for proc in psutil.process_iter(['name']):
                if "revit.exe" in (proc.info['name'] or "").lower():
                    try:
                        p = psutil.Process(proc.pid)
                        if p.cpu_percent(interval=1.0) > 45:
                            p.nice(psutil.HIGH_PRIORITY_CLASS)
                        else:
                            p.nice(psutil.NORMAL_PRIORITY_CLASS)
                    except: pass
            time.sleep(15)

    def safe_purification(self):
        """تطهير آمن يومي [cite: 2026-01-02]"""
        while True:
            temp_paths = [os.environ.get('TEMP'), r"C:\Windows\Temp"]
            for path in temp_paths:
                if not os.path.exists(path): continue
                for item in os.listdir(path):
                    try:
                        full_p = os.path.join(path, item)
                        if os.path.isfile(full_p): os.remove(full_p)
                        elif os.path.isdir(full_p): shutil.rmtree(full_p)
                    except: continue
            time.sleep(86400)

    def save_thermal_history(self, temp, fan, util):
        data = {"ts": time.ctime(), "t": temp, "f": fan, "u": util}
        with open(f"{self.data_path}/thermal_history.json", "a") as f:
            f.write(json.dumps(data) + "\n")

    def log_event(self, tag, msg):
        with open(f"{self.log_path}/Sovereign_4.2.log", "a") as f:
            f.write(f"[{time.ctime()}] {tag}: {msg}\n")

if __name__ == "__main__":
    SovereignOmnibusFinal()
    while True: time.sleep(1)
