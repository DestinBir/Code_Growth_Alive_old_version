from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Product, Cart, Order


def index(request):
    products = Product.objects.all()

    return render(request, 'market/index.html', context={'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'market/detail.html', context={"product": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)
    if product.stock>0:
        if created:
            cart.orders.add(order)
            cart.save()
        else:
            order.quantity += 1
            order.save()
        product.stock = int(product.stock) - 1
    else:
        pass


    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    return render(request, 'market/cart.html', context={'orders': cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()

    return redirect('index')