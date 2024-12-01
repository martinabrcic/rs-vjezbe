import asyncio
import aiohttp

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    return await response.json()

async def filter_cat_facts(cat_list):

    return [fact["fact"] for fact in cat_list if "cat" in fact["fact"].lower()]

async def main():
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [asyncio.create_task(get_cat_fact(session)) for i in range(20)]
        actual_cat_facts = await asyncio.gather(*cat_fact_tasks)
        print(actual_cat_facts)

        filtered_facts = await filter_cat_facts(actual_cat_facts)
    print()

    print("Filtrirane činjenice o mačkama: ")
    print(filtered_facts)
    

asyncio.run(main())