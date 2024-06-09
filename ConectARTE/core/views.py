from django.shortcuts import render
from item.models import Categoría, Item

# Create your views here.

def index(request):
    items = Item.objects.filter(vendido = False)[0:6]
    categorías = Categoría.objects.all()

    return render(request, "core/index.html", {
        "categorías": categorías,
        "items": items,
    })

def contacto(request):
    return render(request, "core/contacto.html")