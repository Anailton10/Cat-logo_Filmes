from django.urls import path
from catalogo import views

urlpatterns = [
    path('cadastro_admin/', views.cadastro_admin, name='cadastro_admin'),

]
