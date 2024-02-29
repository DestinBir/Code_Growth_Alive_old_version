from django.shortcuts import render
import datetime as dt

from .models import *


def home_view(request):
    year = dt.date.today().year
    return render(request, "general/home.html", {'year': year})


def service_view(request):
    services = Service.objects.all()

    return render(request, "general/services.html", {"services": services})


def contact_view(request):
    return render(request, "general/contact-us.html")


def testimonial_view(request):
    testimonials = FeedBack.objects.all()
    return render(request, "general/testimonials.html", {"tests": testimonials})