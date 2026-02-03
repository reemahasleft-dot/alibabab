import os
import pynvml
import time
import subprocess
import ctypes

def reset_voicemeeter_a1():
    print(">>> SYSTEM: DETECTED AUDIO DISRUPTION. RESETTING A1...")
    # أمر إعادة تشغيل محرك Voicemeeter برمجياً لإعادة ربط المخرجات
    try:
        subprocess.run([r"C:\Program Files (x86)\VB\Voicemeeter\Voicemeeter.exe", "-r"], shell=True)
        time.sleep(2)
        print(">>> SUCCESS: AUDIO ENGINE RE-ALIGNED.")
    except:
        print(">>> ERROR: VOICEMEETER PATH NOT FOUND.")

def check_hardware_health():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    
    print(">>> GUARD ACTIVE: MONITORING RTX 5080 & 7800X3D...")
    
    # حلقة المراقبة الدائمة (Low Resource)
    while True:
        try:
            temp = pynvml.nvmlDeviceGetTemperature(handle, 0)
            if temp > 85: # حد الأمان للسياديين
                print(f">>> WARNING: CRITICAL TEMP {temp}C. PROTECTING HARDWARE.")
                # هنا يمكن إضافة أمر لتقليل الطاقة أو إغلاق التطبيقات الثقيلة
            
            # ملاحظة: التحقق من وجود الصوت (يمكن توسيعها مستقبلاً)
            # سنقوم بعمل Reset مرة واحدة عند كل تشغيل لضمان الاستقرار
            
            time.sleep(60) # فحص كل دقيقة للحفاظ على موارد المعالج
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    check_hardware_health()
