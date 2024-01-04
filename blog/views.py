from django.shortcuts import render
from .models import *

def articles(request):

    return render(request, 'blog/articles.html')
