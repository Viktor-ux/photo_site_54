from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *


def index(request):
    posts = Photo.objects.all()
    template = 'photo/index.html'
    context = {'posts': posts,
               'title': 'Главная страница'}
    return render(request, template, context=context)


def portfolio(request):
    posts = Photo.objects.all()
    template = 'photo/portfolio.html'
    context = {'posts': posts,
               'title': 'Мои работы'}
    return render(request, template, context=context)


def price(request):
    template = 'photo/price.html'
    context = {'title': 'Стоимость услуг'}
    return render(request, template, context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404</h1>')