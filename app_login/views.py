from django.shortcuts import render
from app_login.models import User


def home(request):
    return render(request, "home.html")


def login(request):
    novo_login = User()

    novo_login.username = request.POST.get("email")
    novo_login.password = request.POST.get("password")

    novo_login.save()

    # buscar informação no banco de dados com dict
    login = {"login": User.objects.all()}

    return render(request, "login.html", login)
