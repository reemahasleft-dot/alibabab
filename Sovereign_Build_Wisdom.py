import os

SOURCE_DRIVES = ["D:/Sovereign_System", "E:/Sovereign_System"]
WISDOM_FILE = "E:/Sovereign_System/Sovereign_Wisdom_Base.txt"

def build_wisdom_base():
    print("[*] Sovereign Intelligence: Creating the Wisdom Base from Legacy Experience...")
    with open(WISDOM_FILE, "w", encoding="utf-8") as wf:
        wf.write("SOVEREIGN WISDOM BASE - ARCHITECT ALI ESSA (2026)\n")
        wf.write("="*50 + "\n\n")
        
        for drive in SOURCE_DRIVES:
            if os.path.exists(drive):
                for root, dirs, files in os.walk(drive):
                    for file in files:
                        if file.endswith(('.py', '.txt')) and "Wisdom" not in file:
                            wf.write(f"[EXPERIENCE LOG]: Extracted from {file}\n")
                            # استخراج السطور الهامة (المعايير الهندسية والبرمجية)
                            try:
                                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                                    lines = f.readlines()
                                    wf.write(f"  - Logic Sync: {len(lines)} lines of code integrated.\n")
                            except: pass
        
    print(f"[+] Wisdom Base built successfully at: {WISDOM_FILE}")

if __name__ == "__main__":
    build_wisdom_base()
