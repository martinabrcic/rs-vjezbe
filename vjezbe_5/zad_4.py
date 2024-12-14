from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

proizvodi = [
  {"id": 1, "naziv": "Laptop", "cijena": 5000},
  {"id": 2, "naziv": "Miš", "cijena": 100},
  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
  {"id": 4, "naziv": "Monitor", "cijena": 1000},
  {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi, status=200)

async def get_proizvod_id(request):
    proizvod_id = request.match_info['id']

    if proizvod_id == None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            return web.json_response(proizvod, status=200)
    
    return web.json_response({'error': 'Korisnik s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_id)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8081")

async def main():
    await start_server()
    async with aiohttp.ClientSession() as session:
        rezultat = await session.get('http://localhost:8081/proizvodi')
        print("Svi rezultati")
        print(await rezultat.text())
        print()
        rezultat_id = await session.get('http://localhost:8081/proizvodi/4')
        print("Rezultat po ID: ")
        print(await rezultat_id.text())

asyncio.run(main())