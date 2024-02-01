from django.shortcuts import render, redirect
# from .forms import MovieForm
from .models import FilmRegistration


def ver_filmes(request):
    movies = FilmRegistration.objects.all().order_by('-id')
    # seach = request.GET.get('')
    # TODO: Criar seach para pesquisa
    return render(request, 'ver_filmes.html',
                  {'movies': movies})
