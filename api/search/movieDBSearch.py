import json
import urllib
from youtubeSearch import youtube_search
from keys import movieDBkey

movieDBkey = movieDBkey()
resultsLimit = 10


def getMovieFromString(query, releaseYear=False):
    url = "https://api.themoviedb.org/3/search/movie?"
    url += "api_key=" + movieDBkey
    url += "&language=en-US="
    url += "&query=" + query
    url += "&page=1"
    url += "&include_adult=false"
    if releaseYear:
      url += "&primary_release_year=" + str(releaseYear)
    
    movieRes = urllib.urlopen(url)
    movieData = json.loads(movieRes.read())
    
    if movieData['results'][0]['title'].lower() != query.lower():
      movieData['error'] = 'No exact match found'
      return movieData

    return movieData['results'][0]

def getRecommendedMoviesFromString(query, releaseYear=False):

  movieData = getMovieFromString(query, releaseYear=False)
  
  url = "https://api.themoviedb.org/3/movie/"
  url += str(movieData["id"])
  url += "/recommendations?"
  url += "api_key=" + movieDBkey
  url += "&language=en-US"
  url += "&page=1"
  
  similarMovieRes = urllib.urlopen(url)
  similarMovieData = json.loads(similarMovieRes.read())

  result = {
    'movie': movieData,
    'similar': similarMovieData['results'][:10]
  }

  return result