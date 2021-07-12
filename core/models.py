from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField()
    review_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class User(AbstractUser):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    wishlist = models.ManyToManyField(Product)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    score = models.FloatField(default=0.0)
