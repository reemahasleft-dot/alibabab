import tkinter as tk
import psutil
import os

class SovereignNeonV2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 0.6)
        self.root.attributes("-topmost", True)
        self.root.geometry("240x100+1650+20")
        self.root.configure(bg="#050505")

        self.lbl_main = tk.Label(self.root, text="", font=("Consolas", 10, "bold"), bg="#050505", fg="#00FF7F")
        self.lbl_main.pack(expand=True, pady=5)
        
        self.update_stats()
        self.root.mainloop()

    def update_stats(self):
        cpu = psutil.cpu_percent()
        # فحص وجود ملف المزامنة النشط في القرص E
        sync_status = "IDLE"
        if os.path.exists("E:\\Sovereign_Archives\\Elysium_Project"):
            sync_status = "ARCHIVING ACTIVE"
            
        color = "#00FF7F"
        if cpu > 80: color = "#FF3131"
        
        self.lbl_main.config(text=f"ARCHITECT: ALI ESSA\nCPU: {cpu}%\nSTATUS: {sync_status}", fg=color)
        self.root.after(2000, self.update_stats)

if __name__ == "__main__":
    SovereignNeonV2()
