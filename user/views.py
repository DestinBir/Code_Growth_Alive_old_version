from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

from .models import *

User = get_user_model()

def signup(request):
    error = ''
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get('email')
            f_n = request.POST.get('first_name')
            l_n = request.POST.get('last_name')
            user = User.objects.create_user(username=username,password=password, email = email, first_name = f_n, last_name = l_n,)
            login(request, user)
            return redirect("home")
    except:
        error = "Veuillez remplir tous les champs"

    return render(request, 'registration/signup.html', {'error':error})


def logout_user(request):
    logout(request)
    return redirect("home")


def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = "Le mot de passe ou le nom d'utilisateur est incorrect"

    return render(request, 'registration/login.html', {'error':error})

def about_view(request):

    return render(request, 'user/about-ud.html', {'users':''})