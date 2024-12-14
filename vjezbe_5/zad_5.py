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

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi, status=200)

async def get_proizvod_id(request):
    proizvod_id = request.match_info.get('id')

    if proizvod_id is None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            return web.json_response(proizvod, status=200)
    
    return web.json_response({'error': 'Korisnik s traženim ID-em ne postoji'}, status=404)

async def post_proizvod(request):
    
    data = await request.json() 
    proizvod_id = data.get('proizvod_id')
    kolicina = data.get('kolicina')

    proizvod = None
    for p in proizvodi:
        if p["id"] == proizvod_id:
            proizvod = p
            break

    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

    nova_narudzba = {"proizvod_id": proizvod_id, "kolicina": kolicina}
    narudzbe.append(nova_narudzba)

    return web.json_response(narudzbe, status=200)
    
app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_id)
app.router.add_post('/narudzbe', post_proizvod)

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
        print()
        nova_narudzba = {
            "proizvod_id": 5,
            "kolicina": 2
        }
        narudzbe = await session.post('http://localhost:8081/narudzbe', json=nova_narudzba)
        print("Narudzba:")
        print(await narudzbe.text())

if __name__ == '__main__':
    asyncio.run(main())