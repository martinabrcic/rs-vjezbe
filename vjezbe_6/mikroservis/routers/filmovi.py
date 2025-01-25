from fastapi import APIRouter, HTTPException
from models.models_filmovi import Movie
from typing import List, Optional
import json

with open('film.json', 'r') as f:
    filmovi = [Movie(**film) for film in json.load(f)]

router = APIRouter()

@router.get('/filmovi', response_model=List[Movie])
def get_filmovi(
    min_year: Optional[int] = None,
    max_year: Optional[int] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    type: Optional[str] = None
):
    if min_year is not None and min_year < 1900:
        raise HTTPException(status_code=400, detail="Minimalna godina mora biti veća od 1900")
    if max_year is not None and max_year < 1900:
        raise HTTPException(status_code=400, detail="Maksimalna godina mora biti veća od 1900")
    if min_rating is not None and not (0 <= min_rating <= 10):
        raise HTTPException(status_code=400, detail="Minimalna ocjena mora biti između 0 i 10")
    if max_rating is not None and not (0 <= max_rating <= 10):
        raise HTTPException(status_code=400, detail="Maksimalna ocjena mora biti između 0 i 10")
    
    filtrirani_filmovi = filmovi

    def extract_year(year_str):
        if year_str and year_str[:4].isdigit():
            return int(year_str[:4])
        return None

    if min_year:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if extract_year(film.Year) and extract_year(film.Year) >= min_year]
    if max_year:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if extract_year(film.Year) and extract_year(film.Year) <= max_year]
    
    if min_rating:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if film.imdbRating and film.imdbRating >= min_rating]
    if max_rating:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if film.imdbRating and film.imdbRating <= max_rating]
    
    if type:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if film.Type.lower() == type.lower()]
    
    return filtrirani_filmovi

@router.get('/filmovi/title/{title}', response_model=Movie)
def get_film(title: str):
    for film in filmovi:
        if film.Title.lower() == title.lower(): 
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")

@router.get("/filmovi/{imdbID}", response_model=Movie)
def get_film_by_imdb_id(imdbID: str):
    print([film.imdbID for film in filmovi])
    for film in filmovi:
        if film.imdbID.lower() == imdbID.lower():
            return film
    raise HTTPException(status_code=404, detail=f"Film sa IMDb ID {imdbID} nije pronađen.")

