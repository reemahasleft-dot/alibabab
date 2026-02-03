import requests
import json
import time
import os

def ask_sovereign(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "SovereignModel",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        start_time = time.time()
        response = requests.post(url, json=payload)
        duration = time.time() - start_time
        
        result = response.json()['response']
        
        # حفظ السجل على القرص E
        log_path = "E:/Sovereign_System/history_log.txt"
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[{time.ctime()}] Q: {prompt}\nA: {result}\nSpeed: {duration:.2f}s\n{'-'*20}\n")
            
        return result
    except Exception as e:
        return f"Error: {e}. Make sure Ollama is running."

if __name__ == "__main__":
    print("--- Sovereign AI Python Bridge v1.0 ---")
    print("[*] Testing link with RTX 5080 Engine...")
    query = "اعطني نصيحة هندسية سريعة لتحسين كفاءة التصميم المعماري."
    print(f"Response: {ask_sovereign(query)}")
