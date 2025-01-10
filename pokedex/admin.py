from django.contrib import admin
from .models import Pokemon, Trainer

# Register your models here.
@admin.register(Pokemon) #el @ es un decorador, se agreag el pokemon en este caso 

class PokemonAdmin(admin.ModelAdmin):
    pass



@admin.register(Trainer) #el @ es un decorador, se agrega el pokemon en este caso 

class TrainerAdmin(admin.ModelAdmin):
    pass