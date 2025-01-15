from pydantic import BaseModel, Field
from typing import List, Literal

class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = Field(default_factory=list)

admin1 = Admin(
    ime="Marko",
    prezime="Marković",
    korisnicko_ime="mmarkovic",
    email="marko@example.com"
)

admin2 = Admin(
    ime="Ana",
    prezime="Anić",
    korisnicko_ime="aanic",
    email="ana@example.com",
    ovlasti=["dodavanje", "čitanje"]
)

print(admin1)
print(admin2)
