import customtkinter as ctk
import os
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class SovereignUIV2(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN COMMAND CENTER v2.0 - ARCHITECT EDITION")
        self.geometry("500x450")
        
        # حالة النظام الحية
        self.label = ctk.CTkLabel(self, text="Sovereign Intelligence: EVOLVING", font=("Roboto", 22, "bold"))
        self.label.pack(pady=20)

        # شريط الاستبصار (ماذا تعلم النظام اليوم)
        self.insight_box = ctk.CTkTextbox(self, width=400, height=100)
        self.insight_box.pack(pady=10)
        self.update_insights()

        self.boost_btn = ctk.CTkButton(self, text="ENGAGE ULTIMATE PERFORMANCE", command=self.apply_boost, fg_color="green")
        self.boost_btn.pack(pady=10)

        self.audit_btn = ctk.CTkButton(self, text="SYNC WISDOM BASE", command=self.run_audit)
        self.audit_btn.pack(pady=10)

    def update_insights(self):
        # قراءة آخر ما تم تعلمه من كتاب الحكمة المطور
        wisdom_path = "E:/Sovereign_System/Sovereign_Wisdom_2026_Pro.txt"
        if os.path.exists(wisdom_path):
            with open(wisdom_path, "r", encoding="utf-8") as f:
                last_lines = f.readlines()[-3:]
                self.insight_box.insert("0.0", "LATEST INSIGHTS:\n" + "".join(last_lines))

    def apply_boost(self):
        os.system("python E:/Sovereign_System/Sovereign_Proactive_Engine.py")
        self.label.configure(text="Sovereign Status: MAXIMUM POWER")

    def run_audit(self):
        os.system("python E:/Sovereign_System/Sovereign_Wisdom_Evolver.py")
        self.update_insights()

if __name__ == "__main__":
    app = SovereignUIV2()
    app.mainloop()
