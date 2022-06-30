from fastapi import FastAPI

app = FastAPI()

movies = [{"title":"Batman", "year":2021}, {"title":"Joker", "year":2022} ]



@app.get("/")
async def root():
    return {"message":"welcome"}

@app.get("/movies")
def get_movies():
    return movies