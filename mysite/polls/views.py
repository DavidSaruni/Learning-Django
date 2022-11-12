from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# from polls import forms
from .forms import CreateNewList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def index2(response):
    return HttpResponse("This is index 2!")

def home(response):
    return render(response, "main/home.html", {})

def create(request):
    form = CreateNewList()
    return render(request, "main/create.html", {"form":form})