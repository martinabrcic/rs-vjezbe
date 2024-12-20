from aiohttp import web
import aiohttp
import asyncio

async def get_cats(request):
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://catfact.ninja/facts')
        data = await response.json()
        facts = [item["fact"] for item in data.get("data", [])]
    return web.json_response({"facts": facts})

async def get_specific_cats(request):
    amount = int(request.match_info["amount"])
    async with aiohttp.ClientSession() as session:
        tasks = [session.get('https://catfact.ninja/facts') for _ in range(amount)]
        responses = await asyncio.gather(*tasks)
        facts = []
        for response in responses:
            data = await response.json()
            facts.extend([item["fact"] for item in data.get("data", [])])
    return web.json_response({"facts": facts})

app = web.Application()
app.router.add_get('/cats', get_cats)
app.router.add_get('/cat/{amount}', get_specific_cats)

if __name__ == '__main__':
    web.run_app(app, port=8086)