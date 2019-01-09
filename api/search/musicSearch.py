from lastFMSearch import *
from youtubeSearch import youtube_search

def getBestOfArtistTracks(searchTerm):
  LFMsearch = searchLastFMArtistTracks(searchTerm)

  for track in LFMsearch['tracks']:
    track['youtube'] = youtube_search(searchTerm + " " + track['name'])
  
  return LFMsearch

def getBestOfGenreArtists(searchTerm):
  return searchLastFMGenreArtists(searchTerm)

# def getBestOfGenreTracks(searchTerm):
#   LFMsearch = searchLastFMGenreTracks(searchTerm)

#   for track in LFMsearch['tracks']:
#     track['youtube'] = youtube_search(searchTerm + " " + track['name'])

  
#   return LFMsearch