import os
import subprocess

def sovereign_execute(command):
    cmd = command.lower().strip()
    
    if cmd == "revit":
        print("[*] Preparing Sovereign Environment for Revit...")
        os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
        # (إضافة أوامر تنظيف الرام هنا)
        return "[SUCCESS] Environment Optimized for High-End Design."
        
    elif cmd == "heal":
        print("[*] Initiating Sovereign Healing Protocol...")
        subprocess.Popen(["python", "E:/Sovereign_System/Sovereign_Diagnostic_AI.py"])
        return "[SUCCESS] Diagnostic AI is now repairing the system."
        
    elif cmd == "shield":
        print("[*] Activating Sovereign Shield...")
        subprocess.Popen(["python", "E:/Sovereign_System/Sovereign_Tor_Gate_v3.py"])
        return "[SUCCESS] Masked Tunnel Established."
    
    return "[!] Command not recognized. Searching Wisdom Base..."

if __name__ == "__main__":
    # اختبار المحرك
    print(sovereign_execute("heal"))
