from fastapi import FastAPI
from typing import Optional
from models import Film, CreateFilm
filmovi = [
  {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
  {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
  {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
  {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

app = FastAPI()

# @app.get("/filmovi")
# def get_filmovi():
#     return filmovi

# @app.get("/filmovi", response_model=list[Film])
# def get_model_filmovi():
#     return filmovi

@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int):
    pronadeni_film = next((film for film in filmovi if film["id"] == id), None)
    return pronadeni_film

@app.get("/filmovi", response_model=list[Film])
def get_filmovi_by_query(genre: Optional[str] = None, min_godina: int = 2000):
    pronadeni_filmovi = [
        film for film in filmovi 
        if (genre is None or film["genre"] == genre) and film["godina"] >= min_godina
    ]
    return pronadeni_filmovi

@app.post("/filmovi")
def add_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    novi_film = Film(id=new_id, naziv=film.naziv, genre=film.genre, godina=film.godina)
    return novi_film
