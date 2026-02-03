import customtkinter as ctk
import psutil
import os

class SovereignUIV5(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN COMMAND CENTER v5.0 - ABSOLUTE CONTROL")
        self.geometry("800x750")
        
        # حالة السيادة العامة
        self.status_label = ctk.CTkLabel(self, text="SYSTEM STATUS: SUPREME", font=("Roboto", 28, "bold"), text_color="gold")
        self.status_label.pack(pady=20)

        # عداد الكفاءة والحرارة
        self.stats_frame = ctk.CTkFrame(self)
        self.stats_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.cpu_label = ctk.CTkLabel(self.stats_frame, text="7800X3D: 4.20GHz+ (STABLE)", font=("Roboto", 16))
        self.cpu_label.pack(pady=10)

        self.vram_progress = ctk.CTkProgressBar(self.stats_frame, width=500)
        self.vram_progress.pack(pady=10)
        self.vram_progress.set(0.35)

        self.audio_status = ctk.CTkLabel(self.stats_frame, text="Audio: Voicemeeter A1 - OPTIMIZED", font=("Roboto", 14), text_color="cyan")
        self.audio_status.pack(pady=10)

        # زر الاستدعاء الصوتي اليدوي
        self.voice_btn = ctk.CTkButton(self, text="ANNOUNCE SYSTEM STATE", command=self.voice_update)
        self.voice_btn.pack(pady=20)

    def voice_update(self):
        os.system("python E:/Sovereign_System/Sovereign_Sensory_Link.py")

if __name__ == "__main__":
    app = SovereignUIV5()
    app.mainloop()
