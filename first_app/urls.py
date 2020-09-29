"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.urls import path, include

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form_name, name='form'),
    path('topicoform', views.modelform, name='topicoform'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('site', views.site, name='site'),
    path('help', views.help, name='help'),
    path('links', views.links, name='links'),
    path('fivetopicoform', views.fivemodelform, name='fivetopicoform'),
]

