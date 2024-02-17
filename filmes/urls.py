from django.urls import path

from . import views

urlpatterns = [
    path("list_movie/", views.list_movie, name="list_movie"),
    path("register_movie", views.register_movie, name="register_movie"),
    path("detail//<int:id>", views.detail, name="detail"),
]
