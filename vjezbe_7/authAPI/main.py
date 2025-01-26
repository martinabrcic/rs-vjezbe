import hashlib
from fastapi import FastAPI, HTTPException
from typing import List
from models import Korisnik

app = FastAPI()

korisnici = [
  {"korisnicko_ime": "admin", "lozinka_hash" : "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"}, # lozinka = "lozinka123"
  {"korisnicko_ime": "markoMaric", "lozinka_hash" : "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"}, # lozinka = "markoKralj123"
  {"korisnicko_ime": "ivanHorvat", "lozinka_hash" : "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"}, # lozinka = "lllllllllllozinka_123"
  {"korisnicko_ime": "Nada000", "lozinka_hash":"492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"} # lozinka = "blablabla"
]

# Funkcija za hashiranje lozinki
def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

@app.post("/register")
async def dodaj_korisnika(korisnik: Korisnik):
    
    for k in korisnici:
        if k["korisnicko_ime"] == korisnik.korisnicko_ime:
            raise HTTPException(status_code=400, detail="Korisnicko ime vec postoji.")

    novi_korisnik = {
        "korisnicko_ime": korisnik.korisnicko_ime,
        "lozinka_hash": hash_data(korisnik.lozinka)
    }
    korisnici.append(novi_korisnik)
    return {"message": "Korisnik uspjesno registriran.", "korisnicko_ime": korisnik.korisnicko_ime}

@app.post("/login")
async def provjeri_korisnika(korisnik: Korisnik):
    for k in korisnici:
        if k["korisnicko_ime"] == korisnik.korisnicko_ime:
            if k["lozinka_hash"] == hash_data(korisnik.lozinka):
                return {"message": "Prijava uspjesna.", "korisnicko_ime": korisnik.korisnicko_ime}
            else:
                raise HTTPException(status_code=401, detail="Pogresna lozinka.")

    raise HTTPException(status_code=404, detail="Korisnik nije pronadjen.")

@app.get("/users", response_model=List[dict])
async def get_all_users():
    return korisnici