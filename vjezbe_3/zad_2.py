#Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5 sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program se mora izvršavati ~5 sekundi.
import asyncio
import time

korisnici = [{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}]

proizvodi = [{"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}]

async def podaci_s_weba(delay, lista):
    await asyncio.sleep(delay)
    return lista

async def main():

    print (f"Početak: {time.strftime('%X')}")
    korisnici_ispis, proizvodi_ispis = await asyncio.gather(
        podaci_s_weba(3, korisnici),
        podaci_s_weba(5, proizvodi)
    )

    print("Podaci o korisnicima:")
    print(korisnici_ispis)
    print("Podaci o proizvodima:")
    print(proizvodi_ispis)

    print (f"Kraj: {time.strftime('%X')}")
    
asyncio.run(main())       

    


