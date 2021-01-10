from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    # Permet d'afficher les champs dans l'interface d'administration Django
    list_display = ('name', 'ingredients', 'vegetarian', 'price')
    # Permet d'ajouter un champ recherche
    search_fields = ['name']


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
