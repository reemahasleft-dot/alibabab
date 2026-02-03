import keyboard
import os
import pyttsx3

engine = pyttsx3.init()

def instant_sync():
    print("[*] Manual Override: Initiating Instant Sync...")
    os.system("python E:/Sovereign_System/Sovereign_Cloud_Sync.py")
    engine.say("Architectural Assets Synchronized.")
    engine.runAndWait()

# ربط الاختصارات بالسيادة
keyboard.add_hotkey('shift+f12', lambda: instant_sync())

print("[🏁] SOVEREIGN HOTKEYS: Shift+F12 is now your direct link to the Vault.")
keyboard.wait()
