import customtkinter as ctk
import psutil, os, time, pyttsx3, threading

engine = pyttsx3.init()

class SovereignCorePro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN CORE v2026.1 - PROACTIVE EDITION")
        self.geometry("900x850")
        
        self.label = ctk.CTkLabel(self, text="SOVEREIGN AWARENESS: ONLINE", font=("Roboto", 28, "bold"), text_color="cyan")
        self.label.pack(pady=20)

        # عدادات حية للعتاد (CPU & GPU Sim)
        self.vram_meter = ctk.CTkProgressBar(self, width=600)
        self.vram_meter.pack(pady=10)
        self.vram_meter.set(0.0)

        self.log_box = ctk.CTkTextbox(self, width=800, height=400)
        self.log_box.pack(pady=20)

        threading.Thread(target=self.proactive_monitor, daemon=True).start()

    def proactive_monitor(self):
        while True:
            # مراقبة استهلاك المعالج 7800X3D
            cpu_load = psutil.cpu_percent()
            if cpu_load > 80:
                self.update_log(f"[!] Alert: High CPU Load ({cpu_load}%). Stabilizing 7800X3D...")
            
            # محاكاة استشعار Revit
            if "Revit.exe" in [p.name() for p in psutil.process_iter()]:
                self.vram_meter.set(0.7) # رصد استهلاك هندسي
                self.update_log("[+] Architect Mode: Blackwell Cores Synchronized.")
                
            time.sleep(5)

    def update_log(self, message):
        self.log_box.insert("end", f"[{time.ctime()}] {message}\n")
        self.log_box.see("end")

if __name__ == "__main__":
    app = SovereignCorePro()
    app.mainloop()
