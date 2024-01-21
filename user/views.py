from django.shortcuts import render
from .models import *

def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('frontPage')
        else:
            error = "Le mot de passe ou le nom d'utilisateur est incorrect"

    return render(request, 'core/login.html', {'error':error})

def about_view(request):
    users = Admin.objects.all() 

    return render(request, "user/about-us.html", {"users": users})

