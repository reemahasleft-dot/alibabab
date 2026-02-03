import customtkinter as ctk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SovereignUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN COMMAND CENTER v1.0")
        self.geometry("400x300")
        
        self.label = ctk.CTkLabel(self, text="Sovereign Intelligence Active", font=("Roboto", 20))
        self.label.pack(pady=20)

        self.boost_btn = ctk.CTkButton(self, text="ULTIMATE BOOST", command=self.apply_boost)
        self.boost_btn.pack(pady=10)

        self.audit_btn = ctk.CTkButton(self, text="RUN DEEP AUDIT", command=self.run_audit)
        self.audit_btn.pack(pady=10)

    def apply_boost(self):
        os.system("python E:/Sovereign_System/Sovereign_Proactive_Engine.py")
        print("[+] Ultimate Boost Applied via UI.")

    def run_audit(self):
        os.system("python E:/Sovereign_System/Sovereign_Build_Wisdom.py")
        print("[+] Wisdom Base Updated via UI.")

if __name__ == "__main__":
    app = SovereignUI()
    app.mainloop()
