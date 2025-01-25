from fastapi import APIRouter, HTTPException
from models.models_filmovi import Movie
from typing import List
import json

with open('film.json', 'r') as f:
    filmovi = [Movie(**film) for film in json.load(f)]

router = APIRouter()

@router.get('/filmovi', response_model=List[Movie])
def get_filmovi():
    return filmovi

@router.get('/filmovi/title/{title}', response_model=Movie)
def get_film(title: str):
    for film in filmovi:
        if film.Title.lower() == title.lower(): 
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen")

@router.get("/filmovi/{imdbID}", response_model=Movie)
def get_film_by_imdb_id(imdbID: str):
    """Retrieve a movie by its IMDb ID."""
    print([film.imdbID for film in filmovi])
    for film in filmovi:
        if film.imdbID.lower() == imdbID.lower():
            return film
    raise HTTPException(status_code=404, detail=f"Movie with IMDb ID {imdbID} not found.")

