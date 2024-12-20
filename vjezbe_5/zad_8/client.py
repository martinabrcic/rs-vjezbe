import aiohttp
import asyncio

async def get_cat_facts(amount):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8086/cat/{amount}") as response:
            data = await response.json()
            return data.get("facts", [])

async def filter_cat_facts(facts):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8087/facts", json={"facts": facts}) as response:
            data = await response.json()
            return data.get("filtered_facts", [])

async def main():
    amount = 2  
    facts = await get_cat_facts(amount)
    print(f"Dohvaćene činjenice: {facts}")

    filtered_facts = await filter_cat_facts(facts)
    print(f"Filtrirane činjenice: {filtered_facts}")

if __name__ == "__main__":
    asyncio.run(main())


