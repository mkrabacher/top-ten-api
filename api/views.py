# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
from .search.musicSearch import getBestOfArtistTracks, getBestOfGenreArtists, getBestOfGenreTracks
from .search.movieDBSearch import getRecommendedMoviesFromString
from django.http import JsonResponse
import json

# Create your views here.

def getMusicArtist_json(request, artist):
  results = getBestOfArtistTracks(artist)
  return JsonResponse(results)

def getMusicGenreArtists_json(request, genre):
  results = getBestOfGenreArtists(genre)
  return JsonResponse(results)

def getMusicGenreTracks_json(request, genre):
  results = getBestOfGenreTracks(genre)
  return JsonResponse(results)

def getMovieRecomendations_json(request, query):
  params = query.split('&')
  movie = ''
  release = False
  trailer = False
  for param in params:
    elements = param.split('=')
    if elements[0] == 'movie':
      movie = elements[1]
    if elements[0] == 'release':
      release = elements[1]
    if elements[0] == 'trailer':
      trailer = elements[1]
  
  results = getRecommendedMoviesFromString(movie, release, trailer)
  return JsonResponse(results)
