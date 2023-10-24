from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adm
from django.urls import reverse
from hashlib import sha256
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        usuario = authenticate(request, username=email, password=senha)
        if usuario:
            login(request, usuario)
    return HttpResponse('Cadastrado')


def login_admin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # TODO: redirecionar para arena de add os filmes
            return render(request, 'teste.html')
    return render(request, 'login.html')


def logout_admin(request):
    logout(request)
    return redirect(reverse('login_admin'))
