import customtkinter as ctk
import psutil
import os

class SovereignArchUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN ARCHITECT DASHBOARD v3.5")
        self.geometry("600x600")
        
        self.label = ctk.CTkLabel(self, text="Architectural Sovereignty: ACTIVE", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        # مراقب العتاد الهندسي
        self.stats_frame = ctk.CTkFrame(self)
        self.stats_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.vram_label = ctk.CTkLabel(self.stats_frame, text="Checking VRAM Status...", font=("Roboto", 16))
        self.vram_label.pack(pady=10)
        
        self.wisdom_btn = ctk.CTkButton(self, text="INJECT PROJECT WISDOM", command=self.inject_wisdom, fg_color="gold", text_color="black")
        self.wisdom_btn.pack(pady=20)

    def inject_wisdom(self):
        os.system("python E:/Sovereign_System/Sovereign_Wisdom_Evolver.py")
        print("[+] Project Wisdom Synced with Evolved 2026 Standards.")

if __name__ == "__main__":
    app = SovereignArchUI()
    app.mainloop()
