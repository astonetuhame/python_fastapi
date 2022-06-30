from fastapi import FastAPI
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fastapi"
)

mycursor = mydb.cursor()

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
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies = mycursor.fetchall()
    return movies

#get single movie
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
     sql = "SELECT * FROM movies WHERE id = %s"
     val = (movie_id, )
     mycursor.execute(sql, val)
     movie = mycursor.fetchall()
     return movie[0]

#delete a movie
@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    movies.pop(movie_id)
    return {"message":"movie has been deleted successfully"}

#create a movie
@app.post("/create_movie")
def create_movie(movie:dict):
    sql = "INSERT INTO movies(title, year, storyline) VALUES(%s, %s, %s)"
    val = (movie['title'], movie['year'], movie['storyline'])
    mycursor.execute(sql,val)
    mydb.commit()
    return movie

#update movie
@app.post("/update_movie")
def update_movie(movie_id:int, movie:dict):
    sql = "UPDATE movies SET title = %s, year = %s, storyline = %s WHERE id= %s"
    val = (movie['title'], movie['year'], movie['storyline'], movie_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return movie
