import os
import winreg

def set_sovereign_startup():
    print("[*] Sovereign Anchor: Securing Boot Sequence...")
    path = r"E:\Sovereign_System\Sovereign_UI_v4.py"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "SovereignSystem", 0, winreg.REG_SZ, f'python "{path}"')
        winreg.CloseKey(key)
        print("[SUCCESS] Sovereign UI is now anchored to your OS Boot.")
    except Exception as e:
        print(f"[!] Anchor Failed: {e}")

if __name__ == "__main__":
    set_sovereign_startup()
