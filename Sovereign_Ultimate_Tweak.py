import os
def apply_2026_sovereignty():
    print("[*] Applying Global 2026 Performance Standards...")
    # تحسين سرعة فتح البرامج وتقليل زمن الوصول للقرص
    os.system('reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v LargeSystemCache /t REG_DWORD /d 1 /f')
    os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v LastAliveStamp /t REG_DWORD /d 1 /f')
    print("[+] Windows Kernel optimized for Sovereign Architect Ali.")

if __name__ == "__main__":
    apply_2026_sovereignty()
