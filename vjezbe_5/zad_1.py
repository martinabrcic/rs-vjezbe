#Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv, cijena i količina. Pošaljite zahtjev na adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
from aiohttp import web

proizvodi = [{'naziv': 'tipkovnica', 'cijena': 50, 'kolicina': 3},
                 {'naziv': 'miš', 'cijena': 30, 'kolicina': 5}]

async def get_proizvodi(request):
    return web.json_response(proizvodi)
app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
web.run_app(app, port=8081)