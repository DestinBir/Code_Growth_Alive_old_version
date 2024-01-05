from django.shortcuts import render
from .models import *


def about_view(request):
    users = Admin.objects.all() 

    return render(request, "user/about-us.html", {"users": users})
