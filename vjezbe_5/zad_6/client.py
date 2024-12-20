import aiohttp
import asyncio

async def send_request(url, port):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://{url}:{port}/pozdrav')
        return await response.json()

async def main():
    print("Sekvencijalno slanje zahtjeva:")
    microservice1 = await send_request('localhost', 8081)
    print("Prvi mikroservis:", microservice1)
    microservice2 = await send_request('localhost', 8082)
    print("Drugi mikroservis:", microservice2)

    print("\nKonkurentno slanje zahtjeva:")
    microservice1, microservice2 = await asyncio.gather(
        send_request('localhost', 8081),
        send_request('localhost', 8082)
    )
    print("Prvi mikroservis:", microservice1)
    print("Drugi mikroservis:", microservice2)

asyncio.run(main())
