import pandas as pd
import random

#importing CSV file with all the movies I own
#columns in the file include "Title", "Watchabilitty", and "Genre"
    #Title is the movie title for each movie
    #Watchability is if I consider the movie an easy, medium, or hard movie to watch
        #Easy is something I watch all the time and do not need to concentrate while watching
        #Medium is something I watch every now and then but not too often
        #Hard is something I either never watch, something that requires a lot of attention, or a time consuming movie
    #Genre includes Action, Animated, Comedy, Drama, Horror, Romantic Comedy, and Super Hero
my_movies = pd.read_csv('Movies_we_own.csv')

Title_Movie = movies.Title
#List of the all the movie titles

Watchability = movies.Watchabilitty
#Realizing my column Watchabilitty is misspelled with too many Ts at the end. Really need to get my
#laptop's butterfuly keyboard fixed!
#List of all the movies watchability

Genre = movies.Genre
#List of all the movies genres

def random_movie (movies):
    #picks a random movie from CSV file Movies_we_own
    return random.choice(Title_Movie)
    print(random_movie)

def add_movie (movies):
    #add newly purchased movies - Title, Watchability and Genre
    df = (Title_Movie, Watchability, Genre)
    df.append('Spider Man Homecoming', 'Medium', 'Super Hero')
    print(Movies)

def choose_by_genre (movies):
    #choose random movie based on Genre
    random.choice(Genre == Animated)
    print(Title_Movie)

def movie (movie):
    #print or append movies file using codes below
    if input == 1:
      return random_movie()
    elif input == 2:
       return add_movie()
    elif input == 3:
       return choose_by_genre()

assert