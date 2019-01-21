import json
import urllib
from youtubeSearch import youtube_search
from keys import movieDBkey

movieDBkey = movieDBkey()
resultsLimit = 10


def getMovieFromString(query, release_year=False, trailer=False):
    url = "https://api.themoviedb.org/3/search/movie?"
    url += "api_key=" + movieDBkey
    url += "&language=en-US="
    url += "&query=" + query
    url += "&page=1"
    url += "&include_adult=false"

    if release_year:
      url += "&primary_release_year=" + str(release_year)

    
    movieRes = urllib.urlopen(url)
    movieData = json.loads(movieRes.read())
    
    
    if movieData['results'][0]['title'].lower() != query.lower():
      movieData['error'] = 'No exact match found'
      if trailer:
        for movie in movieData['results']:
          movie['trailer'] = youtube_search(movie['name'])
  
      return movieData

    if trailer:
      movieData['results'][0]['trailer'] = youtube_search(movieData['results'][0]['name'])

    return movieData

def getRecommendedMoviesFromString(query, release_year=False, trailer=False):
  movieData = getMovieFromString(query, release_year, False)

  if 'error' in movieData:
    return movieData
  else:
    movieData = movieData['results'][0]


  url = "https://api.themoviedb.org/3/movie/"
  url += str(movieData["id"])
  url += "/recommendations?"
  url += "api_key=" + movieDBkey
  url += "&language=en-US"
  url += "&page=1"
  
  similarMovieRes = urllib.urlopen(url)
  similarMovieData = json.loads(similarMovieRes.read())
  similarMovieData = similarMovieData['results'][:10]

  if trailer:
    for movie in similarMovieData:
      search_term = movie['title']
      search_term += ' movie trailer'
      print 'searching youtube for ' + search_term
      movie['trailer'] = youtube_search(search_term)

  result = {
    'movie': movieData,
    'similar': similarMovieData
  }

  return result