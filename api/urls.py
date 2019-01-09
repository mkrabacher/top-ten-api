from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^json/artist/(?P<artist>\b.+\b)', views.getMusicArtist_json),
    url(r'^json/genre/artists/(?P<genre>\b.+\b)', views.getMusicGenreArtists_json),
    # url(r'^json/genre/tracks/(?P<genre>\b.+\b)', views.getMusicGenreTracks_json),
]
