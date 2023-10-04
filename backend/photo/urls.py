"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.urls import path

from photo.views import about
from photo.views import addpage
from photo.views import contact
from photo.views import index
from photo.views import login
from photo.views import portfolio
from photo.views import price

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000
    path('about/', about, name='about'), # http://127.0.0.1:8000
    path('addpage/', addpage, name='add_page'),
    path('portfolio/', portfolio, name='portfolio'),
    path('price/', price, name='price'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]
