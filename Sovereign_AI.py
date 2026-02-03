import requests
import json

class SovereignAI:
    def __init__(self):
        self.knowledge_base = {
            "التحية": ["مرحباً! أنا النظام السيادي.", "أهلاً وسهلاً بك.", "كيف يمكنني مساعدتك؟"],
            "النظام": ["النظام يعمل بشكل طبيعي.", "جميع المكونات نشطة.", "الأداء في أفضل حالاته."],
            "المساعدة": ["يمكنني مساعدتك في:", "- مراقبة النظام", "- تحليل الأداء", "- تقديم النصائح"],
            "التاريخ": ["الإصدار النهائي 2026", "تم التطوير بواسطة المهندس علي عيسى", "نظام متكامل للمراقبة والتحكم"]
        }
    
    def ask(self, question):
        """الإجابة على الأسئلة"""
        question_lower = question.lower()
        
        for key in self.knowledge_base:
            if key in question_lower:
                import random
                return random.choice(self.knowledge_base[key])
        
        return "أنا هنا لمساعدتك. هل يمكنك توضيح سؤالك أكثر؟"

if __name__ == "__main__":
    print("🤖 النظام السيادي للذكاء الاصطناعي")
    print("اكتب 'خروج' لإنهاء المحادثة")
    print("-" * 40)
    
    ai = SovereignAI()
    
    while True:
        question = input("سؤالك: ")
        if question.lower() in ['خروج', 'exit', 'quit']:
            print("إلى اللقاء! 👋")
            break
        
        answer = ai.ask(question)
        print(f"الجواب: {answer}")
        print("-" * 40)
