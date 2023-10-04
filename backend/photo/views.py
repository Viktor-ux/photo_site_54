from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

menu = ['Обо мне', 'Портфолио', 'Стоимость', 'Контакты', 'Войти']

def index(request):
    posts = Photo.objects.all()
    return render(request, 'photo/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'photo/about.html', {'menu': menu, 'title': 'О нас'})

def categories(request, cat):
    return HttpResponse(f'<h1>Страница категорий {cat}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404</h1>')