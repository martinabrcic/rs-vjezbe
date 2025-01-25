from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Optional

class Writer(BaseModel):
    name: str
    surname: str

class Actor(BaseModel):
    name: str
    surname: str

class Movie(BaseModel):
    # obavezni atributi
    Title: str
    Year: str
    Rated: str
    Runtime: str
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]
    Plot: str
    Writer: List[Writer]

    # neobvezni atributi
    ComingSoon: Optional[bool] = False
    Released: Optional[str] = 'N/A'
    Director: Optional[str] = 'N/A'
    Awards: Optional[str] = 'N/A'
    Poster: Optional[str]
    Metascore: Optional[str] = 'N/A'
    imdbRating: Optional[float] = Field(None, ge=0, le=10)
    imdbVotes: Optional[int] = Field(None, ge=0)
    imdbID: Optional[str]
    Type: Literal["movie", "series"]
    totalSeasons: Optional[int] = None
    Response: Optional[bool] = False
    Images: Optional[List[str]] = []

    @field_validator('Year', mode='before')
    def validate_year(cls, year):
        if len(year) >= 4 and year[:4].isdigit():
            year_int = int(year[:4])
            if year_int <= 1900:
                raise ValueError(f"Year must be greater than 1900, got {year_int}")
            return year
        else:
            raise ValueError(f"Year must start with a valid 4-digit number, got {year}")

    @field_validator('Runtime', mode='before')
    def validate_runtime(cls, runtime):
        if runtime == "N/A": 
            return runtime
        if runtime and runtime[0].isdigit():
            try:
                runtime_int = int(runtime.split()[0])
                if runtime_int <= 0:
                    raise ValueError(f"Runtime must be greater than 0, got {runtime}")
            except ValueError:
                raise ValueError(f"Runtime must be a valid number or 'N/A', got {runtime}")
        else:
            raise ValueError(f"Runtime must start with a valid number or be 'N/A', got {runtime}")
        return runtime
    
    @field_validator('imdbRating', mode='before')
    def validate_imdb_rating(cls, rating):
        if rating == "N/A":
            return None 
        try:
            rating_float = float(rating)
            if not (0 <= rating_float <= 10):
                raise ValueError(f"imdbRating must be between 0 and 10, got {rating}")
        except ValueError:
            raise ValueError(f"imdbRating must be a valid number or 'N/A', got {rating}")
        return rating_float

    @field_validator('imdbVotes', mode='before')
    def validate_imdb_votes(cls, votes):
        if votes == "N/A":
            return None 
        try:
            votes_int = int(votes.replace(",", ""))
            if votes_int <= 0:
                raise ValueError(f"imdbVotes must be greater than 0, got {votes}")
            return votes_int
        except ValueError:
            raise ValueError(f"imdbVotes must be a valid number or 'N/A', got {votes}")

    @field_validator("Actors", mode="before")
    def split_actors(cls, actors):
        if isinstance(actors, str):
            actor_list = []
            for actor in actors.split(","):
                name_parts = actor.strip().split(" ")
                if len(name_parts) >= 2:
                    actor_list.append(Actor(name=name_parts[0], surname=" ".join(name_parts[1:])))
                else:
                    actor_list.append(Actor(name=name_parts[0], surname=""))
            return actor_list
        return actors

    @field_validator("Writer", mode="before")
    def split_writers(cls, writers):
        if isinstance(writers, str):
            writer_list = []
            for writer in writers.split(","):
                name_parts = writer.strip().split(" ")
                if len(name_parts) >= 2:
                    writer_list.append(Writer(name=name_parts[0], surname=" ".join(name_parts[1:])))
                else:
                    writer_list.append(Writer(name=name_parts[0], surname=""))
            return writer_list
        return writers