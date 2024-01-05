from django.shortcuts import render

from .models import *


def home_view(request):
    return render(request, "general/home.html")


def service_view(request):
    services = Service.objects.all()

    return render(request, "general/services.html", {"services": services})


def contact_view(request):
    return render(request, "general/contact-us.html")
