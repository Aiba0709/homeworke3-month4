from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse ("HELLO")

def index(request):
    context = {
        "title": "Главная страница",
        "my_list": [1, 2, 3, 4, 5],
    }
    return render(request, "index.html", context)   

def about(request):
    context = {
        "title": "O нас",
    }
    return render(request, "about.html", context)     

def contacts(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "contacts.html",context )
