import asyncio
import random

async def provjeri_parnost(broj):

    await asyncio.sleep(2)

    if(broj % 2 == 0):
        return (f"Broj + {broj} je paran")
    else:
       return (f"Broj + {broj} je neparan") 

async def main():

    generiranje = [random.randint(1, 100) for i in range(10)]

    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in generiranje]
    rezultati = await asyncio.gather(*zadaci)
    
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())