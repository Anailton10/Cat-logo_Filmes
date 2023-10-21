from django.urls import path
from catalogo import views

urlpatterns = [
    path('adm/', views.adm, name='adm')
]
