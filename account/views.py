from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('CADASTRADO')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html',
                  {'user': user_form})


def login(request):
    if request.method == "POST":
        ...
    else:
        user_form = UserCreationForm()
    return render(request, 'login.html',
                  {'user_form': user_form})
