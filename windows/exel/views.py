from django.shortcuts import render
from django.http import HttpResponse
from .models import Food


def index(request):
    menu1 = Food()
    menu1.name = "Vegitable Burger"
    menu1.img = "1.jpg"
    menu1.price = 10

    menu2 = Food()
    menu2.name = "Beef Burger"
    menu2.img = "2.jpg"
    menu2.price = 15

    menus = [menu1 , menu2]

    return render(request,'home.html',{'menus': menus})
