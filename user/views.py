from django.shortcuts import render
from .models import *

def about_view(request):

    users = User.objects.filter(status = 'Team')

    return render(request, 'user/about-us.html', {'users': users})
