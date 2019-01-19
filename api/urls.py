from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^json/music/artist/(?P<artist>\b.+\b)', views.getMusicArtist_json),
    url(r'^json/music/genre/artists/(?P<genre>\b.+\b)', views.getMusicGenreArtists_json),
    url(r'^json/music/genre/tracks/(?P<genre>\b.+\b)', views.getMusicGenreTracks_json),
    url(r'^json/movie/(?P<movie>\b.+\b)(&release=)(?P<release>\d+)?', views.getMovieRecomendations_json),
    url(r'^json/movie/(?P<movie>\b.+\b)', views.getMovieRecomendations_json),
]
