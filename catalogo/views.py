from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adm
from django.urls import reverse
from hashlib import sha256


def cadastro_admin(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('conf_senha')
        # TODO: Fazer os tratamentos de erros junto com suas mensagens
        if Adm.objects.filter(email=email).exists():
            return HttpResponse('Usuario já existe')
        else:
            if senha != conf_senha:
                return HttpResponse('Senhas não são iguais')

        senha = sha256(senha.encode()).hexdigest()
        novo_usuario = Adm(nome=nome,
                           email=email,
                           senha=senha)
        novo_usuario.save()
    return redirect(reverse('login_admin'))


def login_admin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        senha = sha256(senha.encode()).hexdigest()
        adm = Adm.objects.filter(nome=nome).filter(senha=senha)
        if len(adm) == 0:
            return HttpResponse('Usuario não cadastrado.')
        elif len(adm) > 0:
            request.session['adm'] = adm[0].id
            return redirect(reverse('adicionar_filmes'))

# TODO: adicionar mensagens para melhor interação


def logout_admin(request):
    request.session.flush()
    return redirect(reverse('login_admin'))
