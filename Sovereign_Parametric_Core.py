import requests
import json
import time
import os

WATCH_PATH = "E:/Sovereign_System/Projects_Watch"
LOG_PATH = "E:/Sovereign_System/history_log.txt"
URL = "http://localhost:11434/api/generate"

def ask_sovereign(prompt):
    payload = {"model": "SovereignModel", "prompt": prompt, "stream": False}
    try:
        response = requests.post(URL, json=payload)
        return response.json()['response']
    except Exception as e:
        return f"Error: {e}"

def generate_parametric_code(analysis_result):
    prompt = f"Convert this engineering analysis into a Python script for Revit Dynamo to adjust parameters: {analysis_result}"
    return ask_sovereign(prompt)

if __name__ == "__main__":
    print("--- Sovereign Parametric Core Active (RTX 5080) ---")
    if not os.path.exists(WATCH_PATH): os.makedirs(WATCH_PATH)
    
    while True:
        files = [f for f in os.listdir(WATCH_PATH) if f.endswith('.txt')]
        for file in files:
            full_path = os.path.join(WATCH_PATH, file)
            print(f"[*] Analyzing: {file}")
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # توليد الكود البارامتري
            solution = generate_parametric_code(content)
            
            # حفظ الحل بجانب الملف الأصلي
            solution_file = full_path.replace(".txt", "_solution.py")
            with open(solution_file, "w", encoding="utf-8") as sf:
                sf.write(solution)
            
            # توثيق في سجل الذهب
            with open(LOG_PATH, "a", encoding="utf-8") as log:
                log.write(f"\n[PARAMETRIC {time.ctime()}] File: {file}\nSolution Generated.\n")
            
            # نقل الملف للأرشيف لمنع التكرار
            os.rename(full_path, os.path.join("E:/Sovereign_System/Archive", file))
            print(f"[+] Solution saved and file archived.")
            
        time.sleep(5)
