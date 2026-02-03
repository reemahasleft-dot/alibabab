import time
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# المسارات السيادية
WATCH_PATH = "E:/Sovereign_System/Projects_Watch"
INTERFACE_URL = "http://localhost:11434/api/generate"

class SovereignWatcher(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"[*] New file detected: {event.src_path}")
            self.analyze_design(event.src_path)

    def analyze_design(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            prompt = f"As an engineering assistant, analyze this architectural data and provide an optimization tip: {content}"
            
            payload = {
                "model": "SovereignModel",
                "prompt": prompt,
                "stream": False
            }
            
            response = requests.post(INTERFACE_URL, json=payload)
            advice = response.json()['response']
            
            print(f"\n[Sovereign Analysis]:\n{advice}\n")
            
            # توثيق التحليل التلقائي
            with open("E:/Sovereign_System/history_log.txt", "a", encoding="utf-8") as log:
                log.write(f"\n[AUTO-ANALYSIS {time.ctime()}]\nFile: {file_path}\nAdvice: {advice}\n{'-'*30}\n")
                
        except Exception as e:
            print(f"[!] Analysis Error: {e}")

if __name__ == "__main__":
    if not os.path.exists(WATCH_PATH):
        os.makedirs(WATCH_PATH)
    
    event_handler = SovereignWatcher()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)
    observer.start()
    print(f"--- Sovereign Eye Active: Watching {WATCH_PATH} ---")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
