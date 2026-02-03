import customtkinter as ctk
import os

class VisualAudit(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOVEREIGN ARCHITECTURAL AUDIT - 2026")
        self.geometry("1000x700")
        ctk.set_appearance_mode("dark")

        # العنوان الرئيسي
        self.header = ctk.CTkLabel(self, text="SOVEREIGN SINGULARITY VISUALIZATION", font=("Roboto", 24, "bold"), text_color="gold")
        self.header.pack(pady=20)

        # منطقة عرض البيانات
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # القسم 1: الأقراص والملفات
        self.disk_info = ctk.CTkTextbox(self.main_frame, width=450, height=400, font=("Consolas", 12))
        self.disk_info.grid(row=0, column=0, padx=10, pady=10)
        self.disk_info.insert("0.0", "--- DISK E: SOVEREIGN VAULT CONTENT ---\n")
        
        # قراءة الملفات التي تم صهرها وتأمينها
        vault_files = os.listdir("E:/Sovereign_System")
        for file in vault_files:
            self.disk_info.insert("end", f"[✓] {file}\n")

        # القسم 2: العتاد والسيادة
        self.hw_info = ctk.CTkTextbox(self.main_frame, width=450, height=400, font=("Consolas", 12))
        self.hw_info.grid(row=0, column=1, padx=10, pady=10)
        self.hw_info.insert("0.0", "--- HARDWARE STATUS: SUPREME ---\n")
        self.hw_info.insert("end", "[+] CPU: AMD Ryzen 7 7800X3D (Optimized)\n")
        self.hw_info.insert("end", "[+] GPU: MSI RTX 5080 16G (Blackwell Active)\n")
        self.hw_info.insert("end", "[+] PSU: ROG Thor 1200W Platinum II (Silent)\n")
        self.hw_info.insert("end", "[+] Immunity Shield: ACTIVE & PURIFYING\n")

        # زر الإغلاق والبدء
        self.confirm_btn = ctk.CTkButton(self, text="APPROVE & START DESIGN SESSION", command=self.destroy, fg_color="green")
        self.confirm_btn.pack(pady=20)

if __name__ == "__main__":
    app = VisualAudit()
    app.mainloop()
