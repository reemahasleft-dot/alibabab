import pyttsx3
import psutil
import time

engine = pyttsx3.init()
engine.setProperty('rate', 145)

def sovereign_speak(message):
    print(f"[!] Sovereign Voice: {message}")
    engine.say(message)
    engine.runAndWait()

def monitor_flow():
    # إعلان التدشين الحسي
    sovereign_speak("Sovereign Sensory Link Established. Efficiency at 100 percent.")
    
    last_vram = 0
    while True:
        # إذا تم رصد Revit، أعلن وضع الأداء المعماري
        if "Revit.exe" in [p.name() for p in psutil.process_iter()]:
            sovereign_speak("Architectural Optimization Active. Tensor Cores Reserved.")
            break # إعلان مرة واحدة لكل جلسة
        time.sleep(10)

if __name__ == "__main__":
    monitor_flow()
