from django.shortcuts import render
from django.http import HttpResponse


def adicionar_filmes(request):
    if request.session.get('adm'):
        return render(request, 'filmes.html')
    else:
        return HttpResponse('Faça o login para acessar.')
