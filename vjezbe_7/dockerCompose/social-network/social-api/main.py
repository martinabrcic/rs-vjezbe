from fastapi import FastAPI, HTTPException
from typing import List
from models import Objava, CreateObjava, Login
import datetime
import aiohttp

app = FastAPI()

objave = [{"id": 1, "korisnicko_ime": "admin", "tekst": "Ovo je prva objava.", "vrijeme": 1612345678},
          {"id": 2, "korisnicko_ime": "markoMaric", "tekst": "Ovo je druga objava.", "vrijeme": 1612345679},
          {"id": 3, "korisnicko_ime": "ivanHorvat", "tekst": "Ovo je treca objava.", "vrijeme": 1612345680},
          {"id": 4, "korisnicko_ime": "Nada000", "tekst": "Ovo je cetvrta objava.", "vrijeme": 1612345681}]

@app.get("/objave", response_model=List[Objava])
async def get_all_objave():
    return objave

@app.post("/objava", response_model=Objava)
def create_objava(objava: CreateObjava):
    objava_dict = vars(objava)
    objava_dict["id"] = objave[-1]["id"] + 1 if objave else 1
    date_time = datetime.datetime.now()
    objava_dict["vrijeme"] = date_time.timestamp()
    objave.append(objava_dict)
    return objava_dict

@app.get("/objava/{objava_id}", response_model=Objava)
def dohvati_objavu(objava_id: int):
    for objava in objave:
        if objava["id"] == objava_id:
            return objava
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.post("/objave/korisnici/{korisnicko_ime}/objave", response_model=List[Objava])
async def dohvati_objave_korisnika(korisnicko_ime: str, korisnik_podaci: Login):
    url = "http://auth-api:9000/login"  
    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json=korisnik_podaci.dict()) 
        if response.status == 200: 
            return [objava for objava in objave if objava["korisnicko_ime"] == korisnicko_ime]
        elif response.status == 401: 
            raise HTTPException(status_code=401, detail="Pogrešna lozinka.")
        elif response.status == 404:
            raise HTTPException(status_code=404, detail="Korisnik nije pronađen.")
        else:
            raise HTTPException(status_code=500, detail="Greška u komunikaciji s authAPI.")
