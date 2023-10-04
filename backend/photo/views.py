from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

menu = [
        {"title": 'Обо мне', 'url_name': 'about'},
        {'title': 'Портфолио', 'url_name': 'portfolio'},
        {'title': 'Стоимость', 'url_name': 'price'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
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


def addpage(request):
    return HttpResponse('Добавление')


def portfolio(request):
    return HttpResponse('портфолио')


def price(request):
    return HttpResponse('прайс')


def contact(request):
    return HttpResponse('контакт')


def login(request):
    return HttpResponse('логин')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404</h1>')