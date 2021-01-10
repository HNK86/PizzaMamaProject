from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.


# /menu
def index(request):
    pizzas = Pizza.objects.all().order_by('price')  # Récupère la liste des pizzas et les tries par prix - Collection
    # Récupère les noms et prix des pizzas sous forme de tableau
    # qu'on sort ensuite avec join en les séparants par des virgules
    # pizzas_name_and_price = ", ".join([pizza.name + ': ' + str(pizza.price) + ' €' for pizza in pizzas])

    # return HttpResponse("Les pizzas : " + pizzas_name_and_price)
    return render(request, 'menu/index.html', {
        'pizzas': pizzas,
    })
