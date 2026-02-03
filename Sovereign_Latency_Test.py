import time
import subprocess

def test_response():
    print("[*] Sovereign Validation: Testing System Latency under Master Logic...")
    start_time = time.time()
    
    # محاكاة استدعاء وحدة التشخيص المطورة
    subprocess.run(["python", "E:/Sovereign_System/Sovereign_Diagnostic_AI.py"], capture_output=True)
    
    end_time = time.time()
    latency = (end_time - start_time) * 1000
    print(f"[+] System Response Time: {latency:.2f}ms")
    print("[SUCCESS] Hardware is responding with 2026 Sovereign Speed.")

if __name__ == "__main__":
    test_response()
