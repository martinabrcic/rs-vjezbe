from aiohttp import web

async def first_request(request):
    data = await request.json()
    brojevi = data.get("brojevi", [])
    
    if not isinstance(brojevi, list):
        return web.json_response({"error": "Niste poslali brojeve"}, status=400)
    
    rezultat = sum(brojevi)
    return web.json_response({"zbroj": rezultat})

app = web.Application()
app.router.add_post('/zbroj', first_request)

if __name__ == '__main__':
    web.run_app(app, port=8083)