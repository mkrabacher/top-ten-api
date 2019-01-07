# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
from .search.musicSearch import getBestOfArtistSongList
from django.http import JsonResponse
import json

# Create your views here.

def getArtist_json(request, artist):
  results = getBestOfArtistSongList(artist)
  return JsonResponse(results)