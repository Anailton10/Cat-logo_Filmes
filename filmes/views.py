from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Cadastro_Filmes as cf
from django.contrib import messages
from django.contrib.messages import constants


def adicionar_filmes(request):
    if request.method == "GET":
        if request.session.get('adm'):
            return render(request, 'filmes.html')
        else:
            return HttpResponse('Faça o login para acessar')
    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        sinopse = request.POST.get("sinopse")
        duracao = request.POST.get("duracao")
        autor = request.POST.get("autor")
        capa = request.FILES.get("capa")
        valid = (titulo, sinopse, duracao, autor, capa)
        for v in valid:
            if len(v.strip) == 0:
                messages.add_message(
                    request, constants.ERROR, 'Preencha todos os campos')
                return redirect(reverse('adicionar_filmes'))
        filmes = cf(titulo=titulo,
                    sinopse=sinopse,
                    duracao=duracao,
                    autor=autor,
                    capa=capa
                    )
        filmes.save()
        messages.add_message(
            request, constants.SUCCESS, 'Filme cadastrado com sucesso')
        return redirect(reverse('adicionar_filmes'))


def ver_filmes(request):
    if request.method == "GET":
        filmes = cf.objects.all()
        return render(request, "ver_filmes.html",  {"filmes": filmes})
