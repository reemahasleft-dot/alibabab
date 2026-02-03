# 🤖 بديل نظام الذكاء الاصطناعي
import requests
import json
import time

def ask_sovereign(prompt):
    """سؤال النظام السيادي"""
    try:
        # محاولة الاتصال بـ Ollama
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "SovereignModel",
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(url, json=payload, timeout=10)
        return response.json()['response']
    except:
        return f"❌ الذكاء الاصطناعي غير متصل. سؤال: {prompt}"

# نموذج للاستخدام
if __name__ == "__main__":
    print("🤖 نظام الذكاء الاصطناعي البديل")
    while True:
        question = input("سؤالك: ")
        if question.lower() == "exit":
            break
        answer = ask_sovereign(question)
        print(f"الجواب: {answer}")
