from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


# @login_required

def articles(request):
    articles = Article.objects.all()
    
    return render(request, "blog/articles.html", {'arts':articles})
