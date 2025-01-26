from pydantic import BaseModel, Field
import datetime

class Objava(BaseModel):
    id: int
    korisnicko_ime: str = Field()
    tekst: str = Field()
    vrijeme: datetime.datetime

class CreateObjava(BaseModel):
    korisnik: str = Field()
    tekst: str = Field()

class Login(BaseModel):
    korisnicko_ime: str
    lozinka: str
