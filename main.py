from fastapi import FastAPI

app = FastAPI()

movies = [{"title":"", "year":0},{"title":"Batman", "year":2021}, {"title":"Joker", "year":2022} ]



@app.get("/")
async def root():
    return {"message":"welcome"}

#get all movies
@app.get("/movies")
def get_movies():
    return movies

#get single movie
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
    return movies[movie_id]

