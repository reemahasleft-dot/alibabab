import tkinter as tk
from tkinter import scrolledtext, filedialog
from PIL import Image, ImageTk
import ollama
import threading
import pyttsx3
import os

# === هوية المهندس علي عيسى ===
SYSTEM_PROMPT = """
You are Sovereign Prime. 
Target: Architect Ali Essa.
Hardware: RTX 5080, Ryzen 7800X3D.
Role: Analyze text AND images. Provide technical, high-level engineering advice.
Language: Respond in the SAME language as the user (Arabic if Arabic).
"""

class SovereignVisionAI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SOVEREIGN PRIME [VISION CORE]")
        self.root.geometry("850x950")
        self.root.configure(bg="#050505")
        self.root.attributes("-topmost", True)
        
        self.engine = pyttsx3.init()
        self.image_path = None
        
        self.setup_ui()
        self.speak("Vision Core Online. I can now see what you see, Architect.")

    def speak(self, text):
        def _speak():
            try: self.engine.say(text); self.engine.runAndWait()
            except: pass
        threading.Thread(target=_speak, daemon=True).start()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.add_log(f"IMAGE LOADED: {os.path.basename(file_path)}")
            img = Image.open(file_path)
            img.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(img)
            self.img_label.config(image=photo)
            self.img_label.image = photo 

    def generate_response(self, user_input):
        self.chat_display.insert(tk.END, f"\nARCHITECT: {user_input}\n", "user")
        self.chat_display.see(tk.END)
        self.entry.delete(0, tk.END)
        
        def run_inference():
            try:
                # استخدام Llava للصور و Llama3 للنصوص
                model_name = 'llava' if self.image_path else 'llama3'
                
                msg_content = {'role': 'user', 'content': user_input}
                if self.image_path:
                    msg_content['images'] = [self.image_path]
                    self.add_log(">>> ANALYZING VISUAL DATA WITH TENSOR CORES...")

                stream = ollama.chat(
                    model=model_name,
                    messages=[{'role': 'system', 'content': SYSTEM_PROMPT}, msg_content],
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
                if len(full_response) < 300: self.speak(full_response)
                
                self.image_path = None
                self.img_label.config(image='')
                
            except Exception as e:
                self.chat_display.insert(tk.END, f"\nERROR: {e}\nEnsure 'ollama run llava' is installed.\n", "system")

        threading.Thread(target=run_inference, daemon=True).start()

    def setup_ui(self):
        font_code = ("Consolas", 10)
        tk.Label(self.root, text="SOVEREIGN PRIME // VISION INTEGRATED", fg="#FFD700", bg="#050505", font=("Segoe UI", 14, "bold")).pack(pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(self.root, height=30, width=90, bg="#0a0a0a", fg="#e0e0e0", font=font_code, bd=0)
        self.chat_display.pack(pady=5, padx=20)
        self.chat_display.tag_config("user", foreground="#00D4FF", font=("Consolas", 10, "bold"))
        self.chat_display.tag_config("ai", foreground="#00FF7F")
        self.chat_display.tag_config("system", foreground="#FF3131")

        control_frame = tk.Frame(self.root, bg="#050505")
        control_frame.pack(fill=tk.X, padx=20, pady=5)

        tk.Button(control_frame, text="UPLOAD IMAGE 👁️", command=self.select_image, bg="#1a1a1a", fg="#00D4FF", font=("Consolas", 10)).pack(side=tk.LEFT, padx=5)
        self.img_label = tk.Label(control_frame, bg="#050505")
        self.img_label.pack(side=tk.LEFT, padx=10)

        self.entry = tk.Entry(control_frame, bg="#1a1a1a", fg="white", font=("Segoe UI", 12), insertbackground="white")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.entry.bind("<Return>", lambda e: self.on_enter())
        
        tk.Button(control_frame, text="EXECUTE", command=self.on_enter, bg="#FFD700", fg="black", font=("Consolas", 10, "bold")).pack(side=tk.RIGHT)

    def add_log(self, text):
        self.chat_display.insert(tk.END, f"{text}\n", "system")

    def on_enter(self):
        text = self.entry.get()
        if text: self.generate_response(text)

if __name__ == "__main__":
    SovereignVisionAI().root.mainloop()
