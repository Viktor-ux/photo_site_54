from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

menu = [
        {"title": 'Услуги', 'url_name': 'price'},
        {'title': 'Мои работы', 'url_name': 'portfolio'},
        {'title': 'Подарочный сертификат', 'url_name': 'certificate'},
        {'title': 'Контакты', 'url_name': 'contact'},
        ]


def index(request):
    posts = Photo.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}
    return render(request, 'photo/index.html', context=context)


def post(request):
    ...


def about(request):
    return HttpResponse('обо мне')


def portfolio(request):
    return HttpResponse('Мои работы')


def price(request):
    return HttpResponse('Услуги и цены')


def contact(request):
    return HttpResponse('Контакты')


def certificate(request):
    return HttpResponse('Подарочный сертификат')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404</h1>')