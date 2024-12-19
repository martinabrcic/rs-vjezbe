from aiohttp import web
from asyncio import sleep

async def handle_service_1(request):
    await sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})

app = web.Application()
app.router.add_get('/pozdrav', handle_service_1)

if __name__ == '__main__':
    web.run_app(app, port=8082)