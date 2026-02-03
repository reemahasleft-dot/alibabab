import os, time, subprocess, psutil, random, json, socket, threading, hashlib, sys
from datetime import datetime, timedelta
import logging
from logging.handlers import RotatingFileHandler

# ===================== تهيئة نظام التسجيل (Logging) =====================
def setup_logging():
    log_dir = r'E:\Sovereign_Final\Logs'
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger('SovereignCore')
    logger.setLevel(logging.INFO)
    
    # معالج للملفات مع تدوير
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'sovereign_core.log'),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    
    # معامل التنسيق
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    # إضافة إخراج إلى الكونسول
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()

# ===================== فئة النظام الأساسي =====================
class SovereignSystem:
    def __init__(self):
        self.master_path = r'E:\Sovereign_Final\Dashboard\sovereign_master.html'
        self.live_path = r'E:\Sovereign_Final\Dashboard\sovereign_dashboard_LIVE.html'
        self.backup_path = r'E:\Sovereign_Final\Dashboard\backups\sovereign_dashboard_upgraded.html'
        self.stats_history = {
            'cpu': [], 'gpu_temp': [], 'gpu_util': [], 'memory': [], 'disk': []
        }
        self.system_start_time = datetime.now()
        self.anomaly_count = 0
        self.performance_score = 100
        self.setup_backup_system()
        
        logger.info("Sovereign Core V5.1 Started V5.1")
        
    def setup_backup_system(self):
        """إنشاء نظام نسخ احتياطي تلقائي"""
        backup_dir = r'E:\Sovereign_Final\Backups'
        os.makedirs(backup_dir, exist_ok=True)
        
        # نسخ احتياطي للسيستم
        backup_file = os.path.join(
            backup_dir, 
            f'sovereign_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        )
        
        system_info = {
            'version': 'Sovereign Core V5.1',
            'start_time': self.system_start_time.isoformat(),
            'python_version': sys.version,
            'hostname': socket.gethostname()
        }
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(system_info, f, indent=2)
            
        logger.info(f"Backup created: {backup_file}")
    
    def get_gpu_info(self):
        """جمع معلومات GPU مع معالجة أخطاء محسنة"""
        try:
            # قراءة معلومات NVIDIA GPU
            res = subprocess.check_output(
                ["nvidia-smi", 
                 "--query-gpu=temperature.gpu,fan.speed,utilization.gpu,memory.used,memory.total",
                 "--format=csv,noheader,nounits"], 
                creationflags=0x08000000
            ).decode().strip().split(",")
            
            data = [x.strip() for x in res]
            
            # إضافة معلومات إضافية إذا توفرت
            if len(data) >= 5:
                gpu_mem_used_gb = round(int(data[3]) / 1024, 2)
                gpu_mem_total_gb = round(int(data[4]) / 1024, 2)
                data.extend([str(gpu_mem_used_gb), str(gpu_mem_total_gb)])
            
            return data
            
        except Exception as e:
            logger.warning(f"خطأ في قراءة بيانات GPU: {e}")
            
            # بيانات افتراضية للمحاكاة
            return [
                str(random.randint(30, 45)),  # درجة الحرارة
                str(random.randint(30, 70)),  # سرعة المروحة
                str(random.randint(5, 25)),   # الاستخدام
                "0",  # الذاكرة المستخدمة
                "0"   # الذاكرة الكلية
            ]
    
    def get_system_metrics(self):
        """جمع جميع مقاييس النظام"""
        try:
            gpu = self.get_gpu_info()
            
            # معلومات CPU متقدمة
            cpu_percent = psutil.cpu_percent(interval=0.1)
            cpu_freq = psutil.cpu_freq()
            cpu_freq_current = int(cpu_freq.current) if cpu_freq else 0
            
            # معلومات الذاكرة المتقدمة
            mem = psutil.virtual_memory()
            mem_used_gb = round(mem.used / (1024**3), 2)
            mem_total_gb = round(mem.total / (1024**3), 2)
            mem_available_gb = round(mem.available / (1024**3), 2)
            
            # معلومات القرص المتقدمة
            disk = psutil.disk_usage('E:')
            disk_used_gb = round(disk.used / (1024**3), 2)
            disk_total_gb = round(disk.total / (1024**3), 2)
            
            # معلومات الشبكة
            net_io = psutil.net_io_counters()
            net_sent_mb = round(net_io.bytes_sent / (1024**2), 2)
            net_recv_mb = round(net_io.bytes_recv / (1024**2), 2)
            
            # معلومات العمليات
            process_count = len(psutil.pids())
            
            # وقت التشغيل
            uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
            uptime_str = str(uptime).split('.')[0]
            
            # درجة حرارة النظام (إذا كانت متوفرة)
            try:
                temps = psutil.sensors_temperatures()
                system_temp = temps.get('coretemp', [{}])[0].current if 'coretemp' in temps else 0
            except:
                system_temp = 0
            
            # إضافة البيانات إلى التاريخ
            self._update_history(cpu_percent, float(gpu[0]), float(gpu[2]), 
                                mem.percent, disk.percent)
            
            # حساب Performance Score
            self._calculate_performance_score()
            
            # التحقق من الحالات الشاذة
            self._check_anomalies(cpu_percent, float(gpu[0]), float(gpu[2]))
            
            # تجميع البيانات
            data = {
                # معلومات GPU
                "{gpu_temp}": gpu[0],
                "{gpu_fan}": gpu[1],
                "{gpu_util}": gpu[2],
                "{gpu_mem_used}": gpu[3] if len(gpu) > 3 else "0",
                "{gpu_mem_total}": gpu[4] if len(gpu) > 4 else "0",
                
                # معلومات CPU
                "{cpu_usage}": str(cpu_percent),
                "{cpu_freq}": str(cpu_freq_current),
                "{cpu_cores}": str(psutil.cpu_count(logical=True)),
                "{cpu_cores_physical}": str(psutil.cpu_count(logical=False)),
                "{system_temp}": str(round(system_temp, 1)),
                
                # معلومات الذاكرة
                "{mem_used}": str(mem_used_gb),
                "{mem_total}": str(mem_total_gb),
                "{mem_available}": str(mem_available_gb),
                "{mem_percent}": str(mem.percent),
                
                # معلومات القرص
                "{disk_used}": str(disk_used_gb),
                "{disk_total}": str(disk_total_gb),
                "{disk_free}": str(round(disk.free / (1024**3), 2)),
                "{disk_percent}": str(disk.percent),
                
                # معلومات الشبكة
                "{net_sent}": str(net_sent_mb),
                "{net_recv}": str(net_recv_mb),
                "{net_connections}": str(len(psutil.net_connections())),
                
                # معلومات النظام
                "{uptime}": uptime_str,
                "{process_count}": str(process_count),
                "{boot_time}": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
                "{system_uptime}": str(self.system_start_time.strftime("%Y-%m-%d %H:%M:%S")),
                
                # معلومات التحكم
                "{last_update}": datetime.now().strftime("%H:%M:%S"),
                "{update_timestamp}": str(int(time.time())),
                "{performance_score}": str(self.performance_score),
                "{anomaly_count}": str(self.anomaly_count),
                "{system_health}": "جيد" if self.performance_score > 70 else "تحذير" if self.performance_score > 40 else "حرج"
            }
            
            return data
            
        except Exception as e:
            logger.error(f"خطأ في جمع مقاييس النظام: {e}")
            return {}
    
    def _update_history(self, cpu, gpu_temp, gpu_util, mem, disk):
        """تحديث تاريخ المقاييس"""
        timestamp = time.time()
        
        # حفظ 60 قراءة (3 دقائق بفاصل 3 ثواني)
        max_history = 60
        
        self.stats_history['cpu'].append((timestamp, cpu))
        self.stats_history['gpu_temp'].append((timestamp, gpu_temp))
        self.stats_history['gpu_util'].append((timestamp, gpu_util))
        self.stats_history['memory'].append((timestamp, mem))
        self.stats_history['disk'].append((timestamp, disk))
        
        # تقليص التاريخ إذا تجاوز الحد الأقصى
        for key in self.stats_history:
            if len(self.stats_history[key]) > max_history:
                self.stats_history[key] = self.stats_history[key][-max_history:]
    
    def _calculate_performance_score(self):
        """حساب درجة أداء النظام"""
        try:
            if len(self.stats_history['cpu']) < 10:
                return
            
            # متوسطات قصيرة المدى
            recent_cpu = [v for _, v in self.stats_history['cpu'][-10:]]
            recent_gpu_temp = [v for _, v in self.stats_history['gpu_temp'][-10:]]
            recent_gpu_util = [v for _, v in self.stats_history['gpu_util'][-10:]]
            recent_mem = [v for _, v in self.stats_history['memory'][-10:]]
            
            avg_cpu = sum(recent_cpu) / len(recent_cpu)
            avg_gpu_temp = sum(recent_gpu_temp) / len(recent_gpu_temp)
            avg_gpu_util = sum(recent_gpu_util) / len(recent_gpu_util)
            avg_mem = sum(recent_mem) / len(recent_mem)
            
            # حساب الدرجة (0-100)
            score = 100
            
            # خصم نقاط بناء على المؤشرات
            if avg_cpu > 80:
                score -= 20
            elif avg_cpu > 60:
                score -= 10
                
            if avg_gpu_temp > 80:
                score -= 25
            elif avg_gpu_temp > 70:
                score -= 15
                
            if avg_mem > 85:
                score -= 20
            elif avg_mem > 70:
                score -= 10
                
            # ضمان أن تكون الدرجة بين 0 و 100
            self.performance_score = max(0, min(100, score))
            
        except Exception as e:
            logger.error(f"خطأ في حساب Performance Score: {e}")
    
    def _check_anomalies(self, cpu, gpu_temp, gpu_util):
        """الكشف عن الحالات الشاذة في النظام"""
        try:
            anomaly_detected = False
            
            # عتبات التحذير
            if cpu > 90:
                logger.warning(f"تحذير: استخدام CPU مرتفع: {cpu}%")
                anomaly_detected = True
                
            if gpu_temp > 85:
                logger.warning(f"تحذير: درجة حرارة GPU مرتفعة: {gpu_temp}°C")
                anomaly_detected = True
                
            if gpu_util > 95:
                logger.warning(f"تحذير: استخدام GPU مرتفع: {gpu_util}%")
                anomaly_detected = True
                
            # تحليل اتجاهات الذاكرة
            if len(self.stats_history['memory']) >= 5:
                recent_mem = [v for _, v in self.stats_history['memory'][-5:]]
                if all(recent_mem[i] < recent_mem[i+1] for i in range(len(recent_mem)-1)):
                    logger.warning("تحذير: تسرب محتمل في الذاكرة")
                    anomaly_detected = True
            
            if anomaly_detected:
                self.anomaly_count += 1
                
                # تسجيل الحدث الشاذ
                anomaly_log = {
                    'timestamp': datetime.now().isoformat(),
                    'cpu': cpu,
                    'gpu_temp': gpu_temp,
                    'gpu_util': gpu_util,
                    'total_anomalies': self.anomaly_count
                }
                
                anomaly_file = r'E:\Sovereign_Final\Logs\anomalies.json'
                os.makedirs(os.path.dirname(anomaly_file), exist_ok=True)
                
                anomalies = []
                if os.path.exists(anomaly_file):
                    with open(anomaly_file, 'r', encoding='utf-8') as f:
                        anomalies = json.load(f)
                
                anomalies.append(anomaly_log)
                
                with open(anomaly_file, 'w', encoding='utf-8') as f:
                    json.dump(anomalies, f, indent=2, ensure_ascii=False)
                    
        except Exception as e:
            logger.error(f"خطأ في كشف الحالات الشاذة: {e}")
    
    def generate_dashboard(self):
        """إنشاء وتحديث لوحة التحكم"""
        try:
            # جمع بيانات النظام
            data = self.get_system_metrics()
            
            if not data:
                logger.error("فشل في جمع بيانات النظام")
                return
            
            # قراءة القالب الرئيسي
            if not os.path.exists(self.master_path):
                logger.error(f"الملف الرئيسي غير موجود: {self.master_path}")
                return
            
            with open(self.master_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
            
            # حقن البيانات في القالب
            for key, value in data.items():
                content = content.replace(key, value)
            
            # إضافة تحديث تلقائي مع منع التخزين المؤقت
            random_hash = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
            refresh_meta = f'<meta http-equiv="refresh" content="3; url=sovereign_dashboard_LIVE.html?v={random_hash}">'
            
            if '<meta http-equiv="refresh"' not in content:
                content = content.replace('<head>', f'<head>\n{refresh_meta}')
            
            # إضافة معلومات النظام في JavaScript
            js_data = f"""
            <script>
            // بيانات النظام الحية
            const systemData = {json.dumps(data, ensure_ascii=False)};
            const historyData = {json.dumps({k: v[-20:] for k, v in self.stats_history.items()}, ensure_ascii=False)};
            const lastUpdate = "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}";
            </script>
            """
            
            if '</head>' in content:
                content = content.replace('</head>', f'{js_data}\n</head>')
            
            # حفظ النسخة الحية
            with open(self.live_path, 'w', encoding='utf-8-sig') as f:
                f.write(content)
            
            logger.info(f"Dashboard updated at: {self.live_path}")
            
            # نسخة احتياطية في القرص D
            os.makedirs(os.path.dirname(self.backup_path), exist_ok=True)
            with open(self.backup_path, 'w', encoding='utf-8-sig') as f:
                f.write(content)
            
            # نسخة احتياطية إضافية مع الطابع الزمني
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_live = os.path.join(
                os.path.dirname(self.live_path),
                f'backups/sovereign_dashboard_{timestamp}.html'
            )
            os.makedirs(os.path.dirname(backup_live), exist_ok=True)
            
            with open(backup_live, 'w', encoding='utf-8-sig') as f:
                f.write(content)
            
            # تسجيل إحصاءات النظام
            self._log_system_stats(data)
            
        except Exception as e:
            logger.error(f"خطأ في إنشاء اللوحة: {e}")
    
    def _log_system_stats(self, data):
        """تسجيل إحصاءات النظام"""
        try:
            stats_file = r'E:\Sovereign_Final\Logs\system_stats.json'
            os.makedirs(os.path.dirname(stats_file), exist_ok=True)
            
            stats_entry = {
                'timestamp': datetime.now().isoformat(),
                'data': data,
                'performance_score': self.performance_score,
                'anomaly_count': self.anomaly_count
            }
            
            stats_history = []
            if os.path.exists(stats_file):
                with open(stats_file, 'r', encoding='utf-8') as f:
                    stats_history = json.load(f)
            
            stats_history.append(stats_entry)
            
            # حفظ آخر 1000 قراءة فقط
            if len(stats_history) > 1000:
                stats_history = stats_history[-1000:]
            
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats_history, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            logger.error(f"خطأ في تسجيل إحصاءات النظام: {e}")
    
    def system_cleanup(self):
        """تنظيف النظام وإغلاق آمن"""
        logger.info("System shutting down...")
        
        # حفظ حالة النظام النهائية
        final_state = {
            'shutdown_time': datetime.now().isoformat(),
            'total_runtime': str(datetime.now() - self.system_start_time),
            'final_performance_score': self.performance_score,
            'total_anomalies': self.anomaly_count
        }
        
        state_file = r'E:\Sovereign_Final\Logs\system_state.json'
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(final_state, f, indent=2, ensure_ascii=False)
        
        logger.info("Sovereign Core Closed Successfully")
        logging.shutdown()

# ===================== الدالة الرئيسية =====================
def main():
    """الدالة الرئيسية لتشغيل النظام"""
    system = None
    
    try:
        # إنشاء مثيل النظام
        system = SovereignSystem()
        
        logger.info("Main update loop started ...")
        
        # حلقة التحديث الرئيسية
        cycle_count = 0
        while True:
            cycle_count += 1
            
            # تحديث لوحة التحكم
            system.generate_dashboard()
            
            # تسجيل دوري كل 10 دورات
            if cycle_count % 10 == 0:
                logger.info(f"Update Cycle #{cycle_count} - Performance Score: {system.performance_score}")
            
            # التحقق من استهلاك الموارد كل 30 دورة
            if cycle_count % 30 == 0:
                process = psutil.Process(os.getpid())
                memory_mb = process.memory_info().rss / (1024**2)
                logger.info(f"Memory Usage: {memory_mb:.2f} MB")
                
                if memory_mb > 500:  # إذا تجاوز 500MB
                    logger.warning("استهلاك ذاكرة مرتفع - Restart Recommended")
            
            # الانتظار قبل التحديث التالي
            time.sleep(3)
            
    except KeyboardInterrupt:
        logger.info("تم استقبال إشارة الإيقاف...")
    except Exception as e:
        logger.error(f"خطأ غير متوقع: {e}")
    finally:
        if system:
            system.system_cleanup()

# ===================== نقطة الدخول =====================
if __name__ == "__main__":
    # إظهار رسالة البدء
    print("\n" + "="*60)
    print("🚀 تشغيل Sovereign Core V5.1 - المحرك الخارق")
    print("="*60)
    print(f"وقت البدء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"المضيف: {socket.gethostname()}")
    print(f"مسار اللوحة: E:\\Sovereign_System\\Dashboard")
    print("="*60 + "\n")
    
    # تشغيل النظام
    main()
