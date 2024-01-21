from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


# @login_required

def articles(request):
    return render(request, "blog/articles.html")
