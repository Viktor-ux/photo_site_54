from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Страница Фотографа кошки<h1>')


def categories(request):
    return HttpResponse('<h1>Страница категорий</h1>')
