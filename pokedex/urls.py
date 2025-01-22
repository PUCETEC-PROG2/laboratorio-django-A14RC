# from django.urls import path
# from . import views

# app_name = 'pokedex'

# urlpatterns = [
#     path("", views.index, name="index"), #Pantalla de Pokemons
#     path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    
#     path("trainer/<int:trainer_id>/", views.trainer_detail, name="trainer_details"),
#     path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
#     path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
#     path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
#     path("login/", views.CustomLoginView.as_view(), name = "login"),
# ]

# from django.urls import path
# from . import views

# app_name = 'pokedex'

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("trainers", views.trainers, name="trainers"),
#     path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
#     path("trainer/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
#     path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
#     path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
#     path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
#     path("add_trainer/", views.add_trainer, name="add_trainer"),
#     path("edit_trainer/<int:trainer_id>/", views.edit_trainer, name="edit_trainer"),
#     path("delete_trainer/<int:trainer_id>/", views.delete_trainer, name="delete_trainer"),
#     path("login/", views.CustomLoginView.as_view(), name="login"),
    
# ]


from django.urls import path

from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"), 
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),
    path("all_info_pokemons/", views.all_info_pokemons, name="all_info_pokemons"),
    path("all_info_trainers/", views.all_info_trainers, name="all_info_trainers"),
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("edit_trainer/<int:trainer_id>/", views.edit_trainer, name="edit_trainer"),
    path("delete_trainer/<int:trainer_id>/", views.delete_trainer, name="delete_trainer"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login")
]