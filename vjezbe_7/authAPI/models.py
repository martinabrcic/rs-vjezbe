from pydantic import BaseModel

class Korisnik(BaseModel):
    lozinka: str
    korisnicko_ime: str