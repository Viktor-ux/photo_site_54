from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [
        {"title": 'Услуги', 'url_name': 'price'},
        {'title': 'Мои работы', 'url_name': 'portfolio'},
        {'title': 'Подарочный сертификат', 'url_name': 'certificate'},
        {'title': 'Контакты', 'url_name': 'contact'},
        ]


def index(request):
    posts = Photo.objects.all()
    template = 'photo/index.html'
    context = {'posts': posts,
               'menu': menu,
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


def contact(request):
    template = 'photo/contact.html'
    context = {'title': 'Контактная информация'}
    return render(request, template, context=context)


def certificate(request):
    template = 'photo/certificate.html'
    context = {'title': 'Подарочный сертификат'}
    return render(request, template, context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404</h1>')