import os
import psutil
import time
import threading

def get_network_speed():
    # حساب سرعة الشبكة بالفرق بين قراءتين
    old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    time.sleep(1)
    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    return (new_value - old_value) / 1024 / 1024 # تحويل إلى MB/s

def ping_check(host="8.8.8.8"):
    # فحص سرعة الاستجابة (Ping)
    import subprocess
    try:
        output = subprocess.check_output(f"ping -n 1 {host}", shell=True).decode()
        if "time=" in output:
            return output.split("time=")[1].split("ms")[0] + "ms"
    except:
        return "Offline"
    return "Timeout"

# سيتم دمج هذه الوظائف في واجهة الشيلد الرسومية تلقائياً
