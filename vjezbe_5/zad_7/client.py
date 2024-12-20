import aiohttp
import asyncio

async def fetch_zbroj_data(session, data):
    async with session.post('http://localhost:8083/zbroj', json=data) as response:
        return await response.json()
    
async def fetch_umnozak_data(session, data):
    async with session.post('http://localhost:8084/umnozak', json=data) as response:
        return await response.json()
    
async def fetch_kolicnik_data(session, data):
    async with session.post('http://localhost:8085/kolicnik', json=data) as response:
        return await response.json()

async def main():
    lista = [i for i in range (1, 6)]
    data = {"brojevi": lista}

    async with aiohttp.ClientSession() as session:

        zbroj = fetch_zbroj_data(session, data)
        umnozak = fetch_umnozak_data(session, data)

        response1, response2 = await asyncio.gather(zbroj, umnozak)

        print(response1)
        print(response2)

        kolicnik = fetch_kolicnik_data(session, {"zbroj": response1.get("zbroj"), "umnozak": response2.get("umnozak")})
        response3 = await kolicnik

        print(response3)

if __name__ == '__main__':
    asyncio.run(main())
