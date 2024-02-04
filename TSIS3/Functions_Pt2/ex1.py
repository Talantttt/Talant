# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def goodmovie(movie):
    return movie.get('imdb') > 5.5

print(goodmovie(movies[0]))

#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def goodmovies(movie):
    return [movie for movie in movies if movie.get('imdb')>5.5]

print(goodmovies(movies))

#Write a function that takes a category name and returns just those movies under that category.
def same_genre(movie, name):
    return [movie for movie in movies if movie.get('category') == name]

print(same_genre(movies, 'Suspense'))

#Write a function that takes a list of movies and computes the average IMDB score.
def avg_imdb(movie):
    summa = sum(mov.get('imdb') for mov in movies)
    result = summa/ len(movie)
    return result

print(avg_imdb(movies))

#Write a function that takes a category and computes the average IMDB score.
def avg_imdb_by_genre(movie, name):
    result = sum(mov.get('imdb') for mov in same_genre(movie,name))
    return result/ len(same_genre(movie,name))

print(avg_imdb_by_genre(movies, 'Romance'))