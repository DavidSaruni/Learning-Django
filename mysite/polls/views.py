from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})

def index2(response):
    return HttpResponse("This is index 2!")

def home(response):
    return render(response, "main/home.html", {})