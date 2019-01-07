from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^json/(?P<artist>\b.+\b)', views.getArtist_json),
]
