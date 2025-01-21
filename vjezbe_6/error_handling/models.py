from pydantic import BaseModel

class Automobil(BaseModel):
    id: int
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str