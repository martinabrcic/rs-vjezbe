#Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv, cijena i količina. Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti odgovor s novom listom proizvoda u JSON formatu.

from aiohttp import web

proizvodi = [{'naziv': 'tipkovnica', 'cijena': 50, 'kolicina': 3},
                 {'naziv': 'miš', 'cijena': 30, 'kolicina': 5}]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    data = await request.json()
    print("Dodan proizvod:", data)
    proizvodi.append(data) 
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', post_proizvodi)
web.run_app(app, port=8081)