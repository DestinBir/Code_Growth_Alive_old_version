from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from main import settings

from general.views import *
from blog.views import *
from user.views import *
from market.views import *

urlpatterns = [
    path("admin", admin.site.urls),
    path("services", service_view, name="services"),
    path("contact", contact_view, name="contact-us"),
    path("articles", articles, name="articles"),
    path("article/<int:id>", article, name="article"),
    path("about-us", about_view, name="about-us"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),
    path("signup", signup, name="signup"),
    path("user/<int:id>", user_view, name="user"),
    path('cart/', cart, name='cart'),
    path('cart/delete/', delete_cart, name='delete-cart'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
    path("", home_view, name="home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)