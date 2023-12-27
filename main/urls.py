from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from general.views import *
from blog.views import *
from main import settings
from user.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', home_view, name='home'),
    path('services', service_view, name='services' ),
    path('about', about_view, name='about-us'),
    path('contact', contact_view, name='contact-us'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

