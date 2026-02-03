import psutil
import os
import time
import json
from datetime import datetime

class SovereignCore:
    def __init__(self):
        self.start_time = datetime.now()
        self.log_file = r"E:\Sovereign_Final\Logs\core_system.log"
        
    def get_system_metrics(self):
        """جمع مقاييس النظام"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('E:') if os.path.exists('E:') else psutil.disk_usage('C:')
            
            return {
                "timestamp": datetime.now().isoformat(),
                "cpu_usage": cpu_percent,
                "memory_percent": memory.percent,
                "memory_used_gb": round(memory.used / (1024**3), 2),
                "memory_total_gb": round(memory.total / (1024**3), 2),
                "disk_percent": disk.percent,
                "disk_free_gb": round(disk.free / (1024**3), 2),
                "process_count": len(psutil.pids()),
                "uptime": str(datetime.now() - datetime.fromtimestamp(psutil.boot_time())).split('.')[0]
            }
        except Exception as e:
            return {"error": str(e)}
    
    def run(self):
        """تشغيل النظام"""
        print("[🚀] النظام السيادي الأساسي يعمل...")
        
        while True:
            metrics = self.get_system_metrics()
            
            # حفظ البيانات
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(metrics, ensure_ascii=False) + '\n')
            
            print(f"[📊] CPU: {metrics.get('cpu_usage', 0)}% | RAM: {metrics.get('memory_percent', 0)}%")
            time.sleep(5)

if __name__ == "__main__":
    system = SovereignCore()
    system.run()
