import asyncio
import aiohttp
import time

async def fetch_users(session):
     response = await session.get("https://jsonplaceholder.typicode.com/users")
     return await response.json()

async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
         conc_users = [fetch_users(session) for i in range (5)]
         results = await asyncio.gather(*conc_users)
         print(results)
         
    elapsed_time = time.time() - start_time

    print(f"Vrijeme izvršavanja: {elapsed_time:.2f} sekundi")
    print("")

    lista_1 = [user["name"] for lista in results for user in lista]
    print("Imena korisnika: ", lista_1)
    lista_2 = [user["email"] for lista in results for user in lista]
    print("Email korisnika: ", lista_2)
    lista_3 = [user["username"] for lista in results for user in lista]
    print("Username korisnika: ", lista_3)

asyncio.run(main())
            