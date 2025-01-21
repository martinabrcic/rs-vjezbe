from fastapi import FastAPI, HTTPException
from models import Automobil

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
