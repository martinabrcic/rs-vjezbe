import asyncio

baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
  {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
  {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
  {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
  {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnik):
    await asyncio.sleep(3)

    for user in baza_korisnika:
        if user["korisnicko_ime"] == korisnik["korisnicko_ime"] and user["email"] == korisnik["email"]:
            return await autorizacija(user, korisnik["lozinka"])
        else:
            return f"Korisnik {korisnik} nije pronađen."
    

async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)
    
    for user in baza_lozinka:
        if user["korisnicko_ime"] == korisnik["korisnicko_ime"]:
            if user["lozinka"] == lozinka:
                return f"Korisnik {korisnik["korisnicko_ime"]}: se uspješno autorizirao."
            else:
                return f"Korisnik {korisnik["korisnicko_ime"]}: autorizacija nije bila uspješna."
    
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def main():
    
    provjera_korisnika = { "korisnicko_ime": "ana_anic", "email": "aanic@gmail.com", "lozinka": "lozifffnka123"
    }

    provjera = await autentifikacija(provjera_korisnika)
    print(provjera)
    
asyncio.run(main())

