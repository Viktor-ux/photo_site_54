from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Страница Фотографа кошки<h1>')


def categories(request, cat):
    return HttpResponse(f'<h1>Страница категорий {cat}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404</h1>')