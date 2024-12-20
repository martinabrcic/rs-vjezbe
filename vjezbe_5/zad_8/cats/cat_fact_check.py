from aiohttp import web

async def filter_cat_facts(request):
    data = await request.json()
    facts = data.get("facts", [])
    filtered_facts = [fact for fact in facts if "cat" in fact.lower()]
    return web.json_response({"filtered_facts": filtered_facts})

app = web.Application()
app.router.add_post('/facts', filter_cat_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
