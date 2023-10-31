from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adm
from django.contrib import messages
from django.contrib.messages import constants
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

        if Adm.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect(reverse(cadastro_admin))
        else:
            if senha != conf_senha:
                messages.add_message(
                    request, constants.ERROR, 'Senhas não são iguais')
                return redirect(reverse(cadastro_admin))
            if len(senha) <= 6:
                messages.add_message(
                    request, constants.ERROR, 'Senha curta, informe uma senha com 7 digitos')
                return redirect(reverse(cadastro_admin))
        senha = sha256(senha.encode()).hexdigest()
        novo_usuario = Adm(nome=nome,
                           email=email,
                           senha=senha)
        novo_usuario.save()
        messages.add_message(request, constants.SUCCESS,
                             'Conta cadastrada com sucesso')
    return redirect(reverse('login_admin'))


def login_admin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha = sha256(senha.encode()).hexdigest()
        adm = Adm.objects.filter(email=email).filter(senha=senha)
        if len(adm) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Usuario não existe')
            return redirect(reverse('login_admin'))
        elif len(adm) > 0:
            request.session['adm'] = adm[0].id
            return redirect(reverse('adicionar_filmes'))


def logout_admin(request):
    request.session.flush()
    return redirect(reverse('login_admin'))
