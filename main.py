from fastapi import FastAPI
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fastapi"
)

app = FastAPI()

movies = [{"title":"", "year":0},
          {"title":"Batman", "year":2021}, 
          {"title":"Joker", "year":2022},
          {"title":"Lion King", "year":1999},
          {"title":"Snow white", "year":1998},
          {"title":"Ice Age", "year":2012} ]

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

#delete a movie
@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    movies.pop(movie_id)
    return {"message":"movie has been deleted successfully"}

#create a movie
@app.post("/create_movie")
def create_movie(movie:dict):
    movies.append(movie)
    return movies[-1]

#update movie
@app.post("/update_movie")
def update_movie(movie_id:int, movie:dict):
    movie_to_be_updated = movies[movie_id] #get movie to be updated
    movie_to_be_updated['title'] = movie['title'] #update title
    movie_to_be_updated['year'] = movie['year'] #update year
    movies[movie_id] = movie_to_be_updated #has been updated successfully
    return movie_to_be_updated