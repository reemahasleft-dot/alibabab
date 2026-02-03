import tkinter as tk
from tkinter import ttk
import pynvml
import psutil
import subprocess
import threading
import time

class SovereignShieldV3:
    def __init__(self):
        try:
            pynvml.nvmlInit()
            self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        except:
            self.handle = None
        
        self.root = tk.Tk()
        self.root.title("SCC - SOVEREIGN ARCHITECT v3.0")
        self.root.geometry("500x600")
        self.root.configure(bg="#020202")
        self.root.attributes("-topmost", True)

        self.ping_val = "--"
        self.net_speed = "0.0 MB/s"
        self.combat_active = False

        self.setup_ui()
        self.start_threads()
        self.update_ui_loop()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="[ SOVEREIGN COMMAND CENTER ]", font=("Courier", 18, "bold"), bg="#020202", fg="#FFD700").pack(pady=10)
        tk.Label(self.root, text="ARCHITECT: ALI ESSA", font=("Courier", 10), bg="#020202", fg="#888888").pack()

        # Hardware Info
        self.hw_frame = tk.LabelFrame(self.root, text=" SYSTEM VITALITY ", font=("Courier", 10), bg="#020202", fg="#00BFFF", padx=10, pady=10)
        self.hw_frame.pack(pady=10, padx=20, fill="both")
        
        self.lbl_gpu = tk.Label(self.hw_frame, text="RTX 5080: --", font=("Courier", 12), bg="#020202", fg="#00FF7F")
        self.lbl_gpu.pack(anchor="w")
        
        self.lbl_cpu = tk.Label(self.hw_frame, text="7800X3D: --", font=("Courier", 12), bg="#020202", fg="#FF4500")
        self.lbl_cpu.pack(anchor="w")

        # Network Info
        self.net_frame = tk.LabelFrame(self.root, text=" NETWORK RADAR ", font=("Courier", 10), bg="#020202", fg="#9400D3", padx=10, pady=10)
        self.net_frame.pack(pady=10, padx=20, fill="both")
        
        self.lbl_ping = tk.Label(self.net_frame, text="LATENCY: --", font=("Courier", 12), bg="#020202", fg="#E0FFFF")
        self.lbl_ping.pack(anchor="w")
        
        self.lbl_speed = tk.Label(self.net_frame, text="TRAFFIC: --", font=("Courier", 12), bg="#020202", fg="#FFD700")
        self.lbl_speed.pack(anchor="w")

        # Combat Button
        self.btn_combat = tk.Button(self.root, text="[ ACTIVATE COMBAT MODE ]", command=self.toggle_combat_mode, bg="#2b0040", fg="white", font=("Courier", 11, "bold"), activebackground="#FF0000")
        self.btn_combat.pack(pady=15, fill="x", padx=50)

        # Footer Signature
        tk.Label(self.root, text="(=^･ω･^=) NYA~ ALI ESSA SIGNATURE", font=("Courier", 11), bg="#020202", fg="#FF69B4").pack(pady=15)

    def toggle_combat_mode(self):
        self.combat_active = not self.combat_active
        if self.combat_active:
            self.root.configure(bg="#1a0000")
            self.btn_combat.config(text="[ COMBAT MODE ACTIVE ]", bg="#FF0000")
            # وضع الأداء الأقصى (High Performance)
            subprocess.run("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c", shell=True)
        else:
            self.root.configure(bg="#020202")
            self.btn_combat.config(text="[ ACTIVATE COMBAT MODE ]", bg="#2b0040")
            # الوضع المتوازن (Balanced)
            subprocess.run("powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e", shell=True)

    def network_worker(self):
        while True:
            try:
                # Ping Google DNS
                out = subprocess.check_output("ping -n 1 8.8.8.8", shell=True).decode()
                if "time=" in out:
                    self.ping_val = out.split("time=")[1].split("ms")[0] + "ms"
            except: self.ping_val = "Offline"
            
            old_io = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            time.sleep(1)
            new_io = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            self.net_speed = f"{(new_io - old_io) / 1024 / 1024:.2f} MB/s"

    def start_threads(self):
        threading.Thread(target=self.network_worker, daemon=True).start()

    def update_ui_loop(self):
        if self.handle:
            t = pynvml.nvmlDeviceGetTemperature(self.handle, 0)
            m = pynvml.nvmlDeviceGetMemoryInfo(self.handle).used / 1024**3
            self.lbl_gpu.config(text=f"RTX 5080: {t}C | VRAM: {m:.2f}GB")
        
        self.lbl_cpu.config(text=f"7800X3D: {psutil.cpu_percent()}% LOAD")
        self.lbl_ping.config(text=f"LATENCY (DNS): {self.ping_val}")
        self.lbl_speed.config(text=f"TRAFFIC: {self.net_speed}")
        self.root.after(1000, self.update_ui_loop)

if __name__ == "__main__":
    app = SovereignShieldV3()
    app.root.mainloop()
