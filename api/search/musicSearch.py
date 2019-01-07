from lastFMSearch import searchLastFMArtist
from youtubeSearch import youtube_search

def getBestOfArtistSongList(searchTerm):
  LFMsearch = searchLastFMArtist(searchTerm)

  for track in LFMsearch['tracks']:
    track['youtube'] = youtube_search(searchTerm + " " + track['name'])

  
  return LFMsearch

# searchResults = getBestOfSongList('skrillix')

# print 'Artist:', '\n' + 'Name: ', searchResults['artist']['name'], '\n' + 'url: ', searchResults['artist']['url'], '\n' + 'imageUrl: ', searchResults['artist']['imageUrl'] + '\n \n' + 'Tracks:\n'

# for track in searchResults['tracks']:
#   print 'Name: ', track['name'], '\nurl: ', track['url'], '\nyoutube name: ', track['youtube'][0] + '\nyoutube code: ', track['youtube'][1] + '\n'
