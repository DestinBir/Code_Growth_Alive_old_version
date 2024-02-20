from django.db import models
from django.urls import reverse
from django.utils import timezone

from main.settings import AUTH_USER_MODEL


class Price(models.Model):
    class Statut(models.TextChoices):
        BASIC = "Basic", "Basic", 
        PREMIUM = "Premium", "Premium",
        PRO = "Pro", "Pro"
    
    base_status = Statut.BASIC
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=50, choices=Statut, default=base_status)
    description = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.ForeignKey(Price, related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)

