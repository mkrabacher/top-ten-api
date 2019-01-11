import json
import urllib
from youtubeSearch import youtube_search

LastFMAPIKey = 'd44eace3e6c5ef9f0f25eb0b248ab409'


def getTopArtistTrack(artist):
    artistUrl = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks"
    artistUrl += "&artist=" + artist
    artistUrl += "&api_key=" + LastFMAPIKey
    artistUrl += "&format=json"
    
    artistRes = urllib.urlopen(artistUrl)
    artistData = json.loads(artistRes.read())

    topTrack = {}
    topTrack["artist"] = artistData['toptracks']['track'][0]["artist"]["name"]
    topTrack["track"] = artistData['toptracks']['track'][0]["name"]
    topTrack["url"] = artistData['toptracks']['track'][0]["url"]
    topTrack["youtube"] = youtube_search(topTrack["artist"] + " " + topTrack["track"])

    return topTrack
    


def searchLastFMArtistTracks(searchString):
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


def searchLastFMGenreArtists(searchString):
    url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists"
    url += "&tag=" + searchString
    url += "&api_key=" + LastFMAPIKey
    url += "&format=json"

    print 'Getting data for: ', searchString
    genreRes = urllib.urlopen(url)
    genreData = json.loads(genreRes.read())
    
    genreArtists = []

    for artist in genreData["topartists"]["artist"][:10]:
      returnArtist = {}
      returnArtist["name"] = artist["name"]
      returnArtist["url"] = artist["url"]
      returnArtist["topTrack"] = getTopArtistTrack(artist["name"])

      genreArtists.append(returnArtist)

    return {"artists": genreArtists}


def searchLastFMGenreTracks(searchString):
    url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks"
    url += "&tag=" + searchString
    url += "&api_key=" + LastFMAPIKey
    url += "&format=json"

    print 'Getting data for: ', searchString
    genreRes = urllib.urlopen(url)
    genreData = json.loads(genreRes.read())
    
    genreTracks = []

    for track in genreData["tracks"]["track"][:10]:
      returnTracks = {}
      returnTracks["name"] = track["name"]
      returnTracks["url"] = track["url"]
      returnTracks["topTrack"] = getTopArtistTrack(track["name"])

      genreTracks.append(returnTracks)

    return {"tracks": genreTracks}
