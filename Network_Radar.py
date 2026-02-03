import psutil
import socket
from datetime import datetime

def get_active_connections():
    print(f"\n>>> SOVEREIGN RADAR | TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'PROCESS':<20} | {'LOCAL ADDRESS':<20} | {'REMOTE ADDRESS':<20} | {'STATUS'}")
    print("-" * 80)
    
    connections = psutil.net_connections(kind='inet')
    for conn in connections:
        if conn.status == 'ESTABLISHED':
            try:
                process = psutil.Process(conn.pid).name()
            except:
                process = "Unknown"
            
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "Listening"
            
            print(f"{process[:20]:<20} | {laddr:<20} | {raddr:<20} | {conn.status}")

if __name__ == "__main__":
    get_active_connections()
