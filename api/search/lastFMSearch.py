import json, urllib

def searchLastFMArtist(searchString):
    LastFMAPIKey = 'd44eace3e6c5ef9f0f25eb0b248ab409'

    artistUrl = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks"
    artistUrl += "&artist=" + searchString
    artistUrl += "&api_key=" + LastFMAPIKey
    artistUrl += "&format=json"
    
    print 'Getting data for: ', searchString
    artistRes = urllib.urlopen(artistUrl)
    artistData = json.loads(artistRes.read())

    similarUrl = "http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar"
    similarUrl += "&artist=" + searchString
    similarUrl += "&api_key=" + LastFMAPIKey
    similarUrl += "&format=json"

    similarRes = urllib.urlopen(similarUrl)
    similarData = json.loads(similarRes.read())

    tracks = []
    artist = {}

    for track in artistData['toptracks']['track']:
      tracks.append({"name": track['name'], "url": track['url']})

      if not(hasattr(artist, 'name')):
        artist['name'] = track['artist']['name']

      if not(hasattr(artist, 'url')):
        artist['url'] = track['artist']['url']

      if not(hasattr(artist, 'name')):
        artist['imageUrl'] = track['image'][3]['#text']

    similar = []

    for similarArtist in similarData["similarartists"]["artist"][:5]:
      returnArtist = {}
      returnArtist["artistName"] = similarArtist['name']
      returnArtist["url"] = similarArtist['url']
      returnArtist['imageUrl'] = similarArtist['image'][3]['#text']

      similar.append(returnArtist)


    result = {}
    result["tracks"] = tracks[:10]
    result["artist"] = artist
    result["similar"] = similar

    return result
