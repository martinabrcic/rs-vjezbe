import asyncio
import aiohttp

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    data = await response.json()
    print("Dog fact response:", data)
    
    if 'data' in data:
        
        dog_facts = [fact['attributes']['body'] for fact in data['data']]
        return dog_facts
    else:
        print("No dog facts found in response")
        return []

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    data = await response.json()
    print("Cat fact response:", data)
    return data['fact']

async def mix_facts(lista1, lista2):

    nova_lista = []
    for dog_fact, cat_fact in zip(lista1, lista2):
        if len(dog_fact['fact']) > len(cat_fact['fact']):
            nova_lista.append(dog_fact["fact"])
        else:
            nova_lista.append(cat_fact["fact"])
        return nova_lista

async def main():
    async with aiohttp.ClientSession() as session:
        dog_fact_tasks = [asyncio.create_task(get_dog_fact(session)) for i in range(5)]
        cat_fact_tasks = [asyncio.create_task(get_cat_fact(session)) for i in range(5)]

        dog_cat_facts = await asyncio.gather(*dog_fact_tasks, *cat_fact_tasks)

        #print(dog_cat_facts)
        dog_list = dog_cat_facts[0:4]
        cat_list = dog_cat_facts[5:9]
        print("Dog fact: ", dog_list)
        print()
        print("Cat fact: ", cat_list)
        print()

        mixed_facts = await mix_facts(dog_list, cat_list)
        print(mixed_facts)

asyncio.run(main())