from pydantic import BaseModel, Field
from typing import List, TypedDict

class StolInfo(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float = Field(..., gt=0, description="Ukupna cijena narudžbe mora biti veća od 0")


jelo1 = Jelo(id=1, naziv="Pizza Margherita", cijena=45.5)
jelo2 = Jelo(id=2, naziv="Pasta Carbonara", cijena=40.0)

stol_info = StolInfo(broj=5, lokacija="terasa")

narudzba = RestaurantOrder(
    id=101,
    ime_kupca="Mila",
    stol_info=stol_info,
    jela=[jelo1, jelo2],
    ukupna_cijena=85.5 
)

print(narudzba) 