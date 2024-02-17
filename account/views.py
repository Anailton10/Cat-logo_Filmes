from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("CADASTRADO")
    else:
        user_form = UserCreationForm()
    return render(request, "register.html", {"user": user_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/filmes/list_movie")
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, "login.html", {"user_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("/account/login/")
