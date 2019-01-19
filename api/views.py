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

def getMovieRecomendations_json(request, movie, release=False):
  results = getRecommendedMoviesFromString(movie, release)
  
  return JsonResponse(results)
