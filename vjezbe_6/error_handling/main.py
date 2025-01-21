from fastapi import FastAPI, HTTPException, Query
from models import Automobil, CreateAutomobil

automobili = [
  {"id": 1, "marka": "Audi", "model":"A4", "godina_proizvodnje": 2016, "cijena": 20000, "boja": "srebrna"},
    {"id": 2, "marka": "BMW", "model":"M4","godina_proizvodnje": 2020, "cijena": 30000, "boja": "plava"},
    {"id": 3, "marka": "Renault", "model":"Clio", "godina_proizvodnje": 2005, "cijena": 3000, "boja": "crvena"},
    {"id": 4, "marka": "Fiat", "model":"Punto", "godina_proizvodnje": 1998, "cijena": 1000, "boja": "crna"}
]

app = FastAPI()

@app.get("/automobili/{id}", response_model=Automobil)
def dohvati_automobil(id: int):
  for auto in automobili:
    if auto["id"] == id:
      return auto 
  raise HTTPException(status_code=404, detail="Auto nije pronađen")

@app.get("/automobili")
def dohvati_automobile(min_cijena: int = Query(0, ge=1),
                        max_cijena: int = Query(None, ge=1),
                        min_godina: int = Query(1960, ge=1960),
                        max_godina: int = Query(None, ge=1960)
                       ):
  if max_cijena is not None and min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena ne može biti veća od maksimalne cijene.")
  if max_godina is not None and min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina ne može biti veća od maksimalne godine.")

  filtrirani_automobili = [auto for auto in automobili if 
        (min_cijena is None or auto["cijena"] >= min_cijena) and
        (max_cijena is None or auto["cijena"] <= max_cijena) and
        (min_godina is None or auto["godina_proizvodnje"] >= min_godina) and
        (max_godina is None or auto["godina_proizvodnje"] <= max_godina)
    ]

  return filtrirani_automobili


@app.post("/automobili", response_model=CreateAutomobil)
def kreiraj_automobil(novi_auto: CreateAutomobil):
  
  if any(auto["marka"] == novi_auto.marka and auto["model"] == novi_auto.model and auto["godina_proizvodnje"] == novi_auto.godina_proizvodnje for auto in automobili):
    raise HTTPException(status_code=400, detail="Auto s tim ID već postoji")
  
  auto_id = max([auto["id"] for auto in automobili]) + 1
  cijena_pdv = novi_auto.cijena * 1.25
  
  novi_auto_def = {
    "id": auto_id,
    "marka": novi_auto.marka,
    "model": novi_auto.model,
    "godina_proizvodnje": novi_auto.godina_proizvodnje,
    "cijena": novi_auto.cijena,
    "cijena_pdv": cijena_pdv,
    "boja": novi_auto.boja
  }
  automobili.append(novi_auto_def)
  return novi_auto_def

