from aiohttp import web

async def first_request(request):
    brojevi = await request.json()
    zbroj = brojevi.get("zbroj")
    umnozak = brojevi.get("umnozak")

    if zbroj == 0:
        return web.json_response({"error": "Dijeljenje s nulom nije dozvoljeno"}, status=400)
    
    if not isinstance(zbroj, (int, float)) or not isinstance(umnozak, (int, float)):
        return web.json_response({"error": "Niste poslali brojeve"}, status=400)
    
    kolicnik = umnozak / zbroj
    return web.json_response({"kolicnik": kolicnik})

app = web.Application()
app.router.add_post('/kolicnik', first_request)

if __name__ == '__main__':
    web.run_app(app, port=8085)