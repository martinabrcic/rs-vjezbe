from pydantic import BaseModel, Field
import datetime

class Objava(BaseModel):
    id: int
    korisnik: str = Field()
    tekst: str = Field()
    vrijeme: datetime.datetime

class CreateObjava(BaseModel):
    korisnik: str = Field()
    tekst: str = Field()