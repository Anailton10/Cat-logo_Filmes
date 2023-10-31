from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_filmes/', views.adicionar_filmes, name='adicionar_filmes'),
    path('ver_filmes/', views.ver_filmes, name='ver_filmes'),
]
