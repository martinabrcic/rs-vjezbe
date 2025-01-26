from fastapi import FastAPI, HTTPException
from typing import List
from models import Objava, CreateObjava
import datetime

app = FastAPI()

objave = [{"id": 1, "korisnik": "admin", "tekst": "Ovo je prva objava.", "vrijeme": 1612345678},
          {"id": 2, "korisnik": "markoMaric", "tekst": "Ovo je druga objava.", "vrijeme": 1612345679},
          {"id": 3, "korisnik": "ivanHorvat", "tekst": "Ovo je treca objava.", "vrijeme": 1612345680},
          {"id": 4, "korisnik": "Nada000", "tekst": "Ovo je cetvrta objava.", "vrijeme": 1612345681}]

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

@app.get("/objave/korisnici/{korisnik}/objave", response_model=List[Objava])
def dohvati_objave_korisnika(korisnik: str):
    return [objava for objava in objave if objava["korisnik"] == korisnik]
    