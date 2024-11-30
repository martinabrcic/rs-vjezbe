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

async def autentifikacija(rjecnik, korisnicko_ime, email, lozinka):
    await asyncio.sleep(3)

    korisnicka_imena = [korisnik["korisnicko_ime"] for korisnik in rjecnik]
    emailovi = [korisnik["email"] for korisnik in rjecnik]

    if korisnicko_ime in korisnicka_imena and email in emailovi:
        print(f"Korisnik {korisnicko_ime} je u bazi")
        await autorizacija(baza_lozinka, lozinka)
    else:
        print(f"Korisnik {korisnicko_ime} nije u bazi")
    
    return lozinka
    

async def autorizacija(rjecnik, lozinka):
    await asyncio.sleep(2)
    lozinke = [korisnik["lozinka"] for korisnik in rjecnik]

    if lozinka in lozinke:
        print("Autorizacija uspješna")
    else:
       print("Autorizacija neuspješna")
    
    return lozinka

async def main():
    
    await autentifikacija(baza_korisnika, "mirko123", "mirko123@gmail.com", "lozinka123")
    await autentifikacija(baza_korisnika, "mirko123", "mirko123@gmail.com", "lozinkaa123")
    
asyncio.run(main())

