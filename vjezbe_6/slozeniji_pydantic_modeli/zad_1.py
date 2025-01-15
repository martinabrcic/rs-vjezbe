from pydantic import BaseModel, Field
import datetime

class Izdavac(BaseModel):
    naziv: str
    adresa: str

class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = Field(default_factory=lambda: datetime.datetime.now().year)
    broj_stranica: int
    izdavac: Izdavac

primjer_izdavac = Izdavac(naziv="Martina Brcic", adresa="Adresa 3344")
knjiga_bez_godine = Knjiga(
    naslov="Naslov bez godine",
    ime_autora="Marko",
    prezime_autora="Marković",
    broj_stranica=444,
    izdavac=primjer_izdavac
)

knjiga_s_godinom = Knjiga(
    naslov="Naslov s godinom",
    ime_autora="Ana",
    prezime_autora="Anić",
    godina_izdavanja=1995,
    broj_stranica=555,
    izdavac=primjer_izdavac
)

print(knjiga_bez_godine) 
print(knjiga_s_godinom)
