from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from main import settings

from general.views import *
from blog.views import *
from user.views import *

urlpatterns = [
    path("admin", admin.site.urls),
    path("services", service_view, name="services"),
    path("contact", contact_view, name="contact-us"),
    path("articles", articles, name="articles"),
    path("about-us", about_view, name="about-us"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),
    path("", home_view, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
