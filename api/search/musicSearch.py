from lastFMSearch import *
from youtubeSearch import youtube_search

def getBestOfArtistTracks(searchTerm):
  LFMsearch = searchLastFMArtistTracks(searchTerm)

  for track in LFMsearch['tracks']:
    track['youtube'] = youtube_search(searchTerm + " " + track['name'])
  
  return LFMsearch

def getBestOfGenreArtists(searchTerm):
  LFMsearch = searchLastFMGenreArtists(searchTerm)

  for artist in LFMsearch['artists']:
    artist['youtube'] = youtube_search(searchTerm + " " + artist['name'])

  
  return LFMsearch

# def getBestOfGenreTracks(searchTerm):
#   LFMsearch = searchLastFMGenreTracks(searchTerm)

#   for track in LFMsearch['tracks']:
#     track['youtube'] = youtube_search(searchTerm + " " + track['name'])

  
#   return LFMsearch