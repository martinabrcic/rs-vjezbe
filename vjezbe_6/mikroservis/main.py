from fastapi import FastAPI
from routers.filmovi import router as filmovi_router 

app = FastAPI()

app.include_router(filmovi_router, prefix="/api", tags=["Filmovi"])

@app.get("/")
def home():
    return {"message": "Dobrodošli u FastAPI mikroservis za filmove!"}
