from pydantic import BaseModel
from typing import List, Literal, Optional

class Writer(BaseModel):
    name: str
    surname: str

class Actor(BaseModel):
    name: str
    surname: str

class Movie(BaseModel):
    title: str
    year: int
    rated: str
    released: Optional[str]
    runtime: str
    genre: str
    director: Optional[str]
    writer: List[Writer]
    actors: List[Actor]
    plot: str
    language: str
    country: str
    awards: Optional[str]
    poster: str
    metascore: int
    imbdRating: float
    imbdVotes: int
    imbdID: str
    type: Literal["movie", "series"]
    totalSeasons: int
    response: bool
    rating: float
    images: List[str]