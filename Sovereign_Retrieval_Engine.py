import os
import glob

VAULT_PATH = "E:/Sovereign_System/Core_Intelligence/Legacy_Recovered"

def search_wisdom(query):
    print(f"[*] Sovereign Radar: Searching for '{query}' in the Vault...")
    # البحث في كافة الملفات المهضومة والمسترجعة
    files = glob.glob(os.path.join(VAULT_PATH, f"*{query}*"))
    if files:
        for f in files:
            print(f"[+] Found Match: {os.path.basename(f)}")
            # (هنا يمكن فتح الملف أو عرض محتواه هندسياً)
    else:
        print("[!] No direct match. Checking Global 2026 Standards...")

if __name__ == "__main__":
    # اختبار المحرك بكلمة "كود" التي استرجعناها اليوم
    search_wisdom("كود")
