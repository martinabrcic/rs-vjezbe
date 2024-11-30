import asyncio

osjetljivi_podaci = [{"prezime": "Brcic", "broj_kartice": "500012345678", "CVV": "111"},
    {"prezime": "Macic", "broj_kartice": "100012345678", "CVV": "224"},
    {"prezime": "Lukic", "broj_kartice": "200012345678", "CVV": "565"}]

async def secure_data(rjecnik):

    await asyncio.sleep(3)
    enkriptirano = {'prezime': rjecnik['prezime'],
                    'broj_kartice': str(hash(rjecnik['broj_kartice'])),
                    'CVV' : str(hash(rjecnik['CVV']))
                    }
    return enkriptirano


async def main():

    zadaci = [secure_data(data) for data in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)

    for rez in rezultati:
        print(rez)

asyncio.run(main())

