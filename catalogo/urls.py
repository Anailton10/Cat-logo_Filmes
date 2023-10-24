from django.urls import path
from catalogo import views

urlpatterns = [
    path('cadastro_admin/', views.cadastro_admin, name='cadastro_admin'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),


]
