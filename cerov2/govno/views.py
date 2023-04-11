from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return render(request,'index.html')
    #data = {"header": "Передача параметров в шаблон Django",
            #"message": "Загружен шаблон templates\govno\index_app1.html"}
    #return render(request, "index_app1.html", context=data)
    #header = "Персональные данные"
   # langs = ["Английский", "Немецкий", "Испанский"]
    #user = {"name": "Максим", "age" :30 }
   # addr = ("Виноградная", 23,45)
    #data = {"header" : header, "langs":langs, "user": user, "address": addr,}
    return render(request,"home.html")

