from django.shortcuts import render
from django.http import HttpResponse


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

        # TODO: Adicionar validacoes
        
        filmes = cf(titulo=titulo,
        sinopse=sinopse,
        duracao=duracao,
        autor=autor,
        capa=capa
        )
        filmes.save()
        

def ver_filmes(request):
    if request.method == "GET":
        filmes = cf.objects.all()
        return render(request, "ver_filmes.html",  {"filmes": filmes)