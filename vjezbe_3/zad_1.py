#Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom. Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez korištenja asyncio.gather() i asyncio.create_task() funkcija.
import asyncio
import time

async def podaci_s_weba():
    print('Dohvaćanje podataka...')
    lista = [i for i in range(1, 11)]
    await asyncio.sleep(3)
    print('Podaci dohvaćeni: ')
    return lista


async def main():
    lista_brojeva = await podaci_s_weba()
    print(f'Podaci: {lista_brojeva}')

asyncio.run(main())
































































































































