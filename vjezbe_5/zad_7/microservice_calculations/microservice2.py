from aiohttp import web

async def first_request(request):
    data = await request.json()
    brojevi = data.get("brojevi", [])
    
    if not isinstance(brojevi, list):
        return web.json_response({"error": "Niste poslali brojeve"}, status=400)
    
    umnozak = 1
    for broj in brojevi:
        umnozak *= broj
    return web.json_response({"umnozak": umnozak})

app = web.Application()
app.router.add_post('/umnozak', first_request)

if __name__ == '__main__':
    web.run_app(app, port=8084)