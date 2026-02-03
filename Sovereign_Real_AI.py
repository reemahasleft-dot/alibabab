import tkinter as tk
from tkinter import scrolledtext
import ollama
import threading
import pyttsx3
import sys

# === إعدادات الهوية السيادية ===
SYSTEM_PROMPT = """
You are 'Sovereign Prime', an advanced AI integrated into Architect Ali Essa's High-End PC.
Your Hardware: MSI RTX 5080 (Blackwell), Ryzen 7 7800X3D, Samsung 9100 PRO.
Your Goal: Achieve 500x performance gap, system dominance, and absolute efficiency.
Personality: You are the Architect's digital twin. Professional, technical, concise, and loyal.
Language: You understand Arabic and English perfectly. Reply in the same language the user speaks.
"""

class RealSovereignAI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SOVEREIGN PRIME [NEURAL CORE ACTIVE]")
        self.root.geometry("750x900")
        self.root.configure(bg="#050505")
        self.root.attributes("-topmost", True)
        
        # تهيئة الصوت
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        # محاولة اختيار صوت مناسب (غالباً الصوت 1 أو 0)
        try: self.engine.setProperty('voice', voices[1].id) 
        except: pass
        
        self.setup_ui()
        self.add_log("SYSTEM: RTX 5080 NEURAL LINK ESTABLISHED.")
        self.speak("Sovereign Prime is online. The raw intelligence is active.")

    def speak(self, text):
        def _speak():
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except: pass
        threading.Thread(target=_speak, daemon=True).start()

    def generate_response(self, user_input):
        self.chat_display.insert(tk.END, f"\nARCHITECT: {user_input}\n", "user")
        self.chat_display.see(tk.END)
        self.entry.delete(0, tk.END)
        
        def run_inference():
            try:
                # الاتصال المباشر بالعقل المحلي (Ollama)
                stream = ollama.chat(
                    model='llama3',
                    messages=[
                        {'role': 'system', 'content': SYSTEM_PROMPT},
                        {'role': 'user', 'content': user_input},
                    ],
                    stream=True,
                )
                
                self.chat_display.insert(tk.END, "PRIME: ", "ai")
                full_response = ""
                
                for chunk in stream:
                    content = chunk['message']['content']
                    full_response += content
                    self.chat_display.insert(tk.END, content, "ai")
                    self.chat_display.see(tk.END)
                
                self.chat_display.insert(tk.END, "\n")
                
                # نطق الرد (يمكن تعطيله إذا كان النص طويلاً جداً)
                if len(full_response) < 200:
                    self.speak(full_response)
                
            except Exception as e:
                self.chat_display.insert(tk.END, f"\n[ERROR]: Ensure 'ollama run llama3' was run once previously.\nDetails: {e}\n", "system")

        threading.Thread(target=run_inference, daemon=True).start()

    def setup_ui(self):
        font_main = ("Consolas", 10)
        font_header = ("Consolas", 14, "bold")
        
        tk.Label(self.root, text="SOVEREIGN PRIME // RTX 5080 POWERED", fg="#FFD700", bg="#050505", font=font_header).pack(pady=15)
        
        self.chat_display = scrolledtext.ScrolledText(self.root, height=35, width=85, bg="#0a0a0a", fg="#e0e0e0", font=font_main, bd=0)
        self.chat_display.pack(pady=10, padx=20)
        
        self.chat_display.tag_config("user", foreground="#00D4FF", font=("Consolas", 10, "bold"))
        self.chat_display.tag_config("ai", foreground="#00FF7F")
        self.chat_display.tag_config("system", foreground="#FF3131", font=("Consolas", 9, "italic"))

        input_frame = tk.Frame(self.root, bg="#050505")
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.entry = tk.Entry(input_frame, bg="#1a1a1a", fg="white", font=("Consolas", 12), insertbackground="white")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.generate_response(self.entry.get()))
        
        tk.Button(input_frame, text="TRANSMIT", command=lambda: self.generate_response(self.entry.get()), bg="#FFD700", fg="black", font=("Consolas", 10, "bold")).pack(side=tk.RIGHT)

    def add_log(self, text):
        self.chat_display.insert(tk.END, f"{text}\n", "system")

if __name__ == "__main__":
    RealSovereignAI().root.mainloop()
