import customtkinter as ctk
import os
import glob
import subprocess

class SovereignUIV4_Updated(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN COMMAND CENTER v4.1 - EXECUTIVE EDITION")
        self.geometry("700x600")
        
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Type Command (Revit, Heal, Shield) or Search...", width=500)
        self.search_entry.pack(pady=20)
        
        self.action_btn = ctk.CTkButton(self, text="EXECUTE / SEARCH", command=self.process_input, fg_color="gold", text_color="black")
        self.action_btn.pack(pady=5)

        self.results_box = ctk.CTkTextbox(self, width=600, height=300)
        self.results_box.pack(pady=20)

    def process_input(self):
        query = self.search_entry.get().lower().strip()
        self.results_box.insert("end", f"\n[*] Processing: {query}...\n")
        
        # 1. محاولة التنفيذ (Executive Commands)
        commands = {
            "revit": "Preparing Environment for Architect Ali...",
            "heal": "Initiating Diagnostic AI v1.1...",
            "shield": "Activating Tor Masked Tunnel..."
        }
        
        if query in commands:
            if query == "heal":
                subprocess.Popen(["python", "E:/Sovereign_System/Sovereign_Diagnostic_AI.py"])
            elif query == "shield":
                subprocess.Popen(["python", "E:/Sovereign_System/Sovereign_Tor_Gate_v3.py"])
            self.results_box.insert("end", f"[EXEC]: {commands[query]}\n")
            return

        # 2. إذا لم يكن أمراً، ابحث في الخزنة
        vault_path = "E:/Sovereign_System/Core_Intelligence/Legacy_Recovered"
        matches = glob.glob(os.path.join(vault_path, f"*{query}*"))
        if matches:
            for m in matches:
                self.results_box.insert("end", f"[FOUND]: {os.path.basename(m)}\n")
        else:
            self.results_box.insert("end", "[!] No command or file matched.\n")

if __name__ == "__main__":
    app = SovereignUIV4_Updated()
    app.mainloop()
