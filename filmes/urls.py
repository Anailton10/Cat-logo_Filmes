from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_filmes/', views.adicionar_filmes, name='adicionar_filmes'),


]
