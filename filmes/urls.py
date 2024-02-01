from django.urls import path
from . import views

urlpatterns = [
    path('ver_filmes/', views.ver_filmes, name='ver_filmes')
]
