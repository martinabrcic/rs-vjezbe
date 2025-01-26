from pydantic import BaseModel, Field
from datetime import timestamp

class Objava(BaseModel):
    id: int
    korisnik: str = Field(ge=0, le=20)
    teks: str = Field(ge=0, le=280)
    vrijeme: timestamp

class CreateObjava(BaseModel):
    korisnik: str = Field(ge=0, le=20)
    teks: str = Field(ge=0, le=280)