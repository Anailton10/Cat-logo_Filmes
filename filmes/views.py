from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import FilmRegistration, Category
from django.http import HttpResponse


def list_movie(request):
    movies = FilmRegistration.objects.all().order_by('-id')
    categorys = Category.objects.all()
    category_id = request.GET.get('category')
    search = request.GET.get('search')
    if search:
        movies = movies.filter(title__icontains=search)

    if category_id:
        movies = movies.filter(category_id=category_id)
    return render(request, 'list_movie.html',
                  {'movies': movies,
                   'categorys': categorys})


def register_movie(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
        else:
            return render(request, 'register_movie.html',
                          {'movie_form': movie_form, })
    else:
        movie_form = MovieForm()
        return render(request, 'register_movie.html',
                      {'movie_form': movie_form, })


def detail(request, id):
    movies = FilmRegistration.objects.filter(id=id)
    return render(request, 'detail.html',
                  {'movies': movies})
