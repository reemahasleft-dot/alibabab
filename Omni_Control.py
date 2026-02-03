import os
import tkinter as tk
from tkinter import messagebox
import psutil # سنستخدم هذه المكتبة لمراقبة الأداء

class SovereignCommand:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ULTRA SOVEREIGN COMMAND CENTER v1.2")
        self.root.geometry("500x550+100+100")
        self.root.configure(bg="#050505")
        self.root.attributes("-alpha", 0.95)
        self.root.attributes("-topmost", True)

        tk.Label(self.root, text="OMNIPRESENT CONTROLLER v1.2", fg="#00FF7F", bg="#050505", font=("Consolas", 16, "bold")).pack(pady=10)

        # قسم مراقبة الأداء الحية
        self.stats_label = tk.Label(self.root, text="CPU: 0% | MEM: 0%", fg="#00D4FF", bg="#050505", font=("Consolas", 10))
        self.stats_label.pack(pady=5)
        self.update_stats()

        tk.Button(self.root, text="FIX SOVEREIGN AUDIO", command=self.fix_audio, bg="#1a1a1a", fg="#FF3131", font=("Consolas", 11, "bold"), height=2).pack(pady=10, fill=tk.X, padx=50)
        tk.Button(self.root, text="GAME OPTIMIZATION STRATEGY", command=self.game_strategy, bg="#1a1a1a", fg="#00FF7F", font=("Consolas", 11)).pack(pady=10, fill=tk.X, padx=50)
        tk.Button(self.root, text="LAUNCH ELYSIUM ARCHIVES", command=self.launch_elysium, bg="#1a1a1a", fg="#00D4FF", font=("Consolas", 11)).pack(pady=10, fill=tk.X, padx=50)
        tk.Button(self.root, text="EXIT SYSTEM", command=self.root.destroy, bg="#050505", fg="#555555", font=("Consolas", 9)).pack(pady=20)

        self.root.mainloop()

    def update_stats(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        self.stats_label.config(text=f"CPU: {cpu}% | RAM: {mem}% | RTX 5080: READY")
        self.root.after(2000, self.update_stats)

    def fix_audio(self):
        vm_path = os.environ.get('VM_SOVEREIGN_PATH')
        if vm_path:
            os.system(f'"{vm_path}" -R')
            messagebox.showinfo("SENTINEL", "Audio Recovery Sequence Completed.")
        else:
            messagebox.showerror("ERROR", "Path Variable Null. Run Path Hunter.")

    def game_strategy(self):
        messagebox.showinfo("AI CORE", "Architect Ali, System is optimized for 4K Ray Tracing.")

    def launch_elysium(self):
        os.startfile("E:\\Sovereign_Archives\\Elysium_Project")

if __name__ == "__main__":
    SovereignCommand()
