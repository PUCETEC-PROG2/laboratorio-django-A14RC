from django.contrib import admin
from .models import Pokemon

# Register your models here.
@admin.register(Pokemon) #el @ es un decorador, se agreag el pokemon en este caso 

class PokemonAdmin(admin.ModelAdmin):
    pass