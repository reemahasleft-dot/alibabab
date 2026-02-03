import customtkinter as ctk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SovereignUIV3(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN COMMAND CENTER v3.0 - INNOVATION CORE")
        self.geometry("600x550")
        
        self.label = ctk.CTkLabel(self, text="Sovereign Innovation Matrix: ACTIVE", font=("Roboto", 22, "bold"))
        self.label.pack(pady=20)

        # عرض القدرات الهجينة المبتكرة
        self.innovation_frame = ctk.CTkFrame(self)
        self.innovation_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.add_innovation_btn("HYBRID LATENCY SHIELD", "E:/Sovereign_System/Core_Intelligence/Sovereign_Network.py")
        self.add_innovation_btn("NEURAL HARDWARE GOVERNOR", "E:/Sovereign_System/Sovereign_Power_Audit.py")
        self.add_innovation_btn("AUTONOMOUS SYSTEM HEALER", "E:/Sovereign_System/Sovereign_Diagnostic_AI.py")

    def add_innovation_btn(self, name, path):
        btn = ctk.CTkButton(self.innovation_frame, text=name, command=lambda: os.system(f"python {path}"))
        btn.pack(pady=5, padx=10, fill="x")

if __name__ == "__main__":
    app = SovereignUIV3()
    app.mainloop()
