from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def do_login(self):
        #
        pass

    def do_forget_password(self):
        #
        pass

    class Meta:
        abstract = True


class Admin(User):
    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def update_item(self, item):
        pass

class Customer(User):
    points = models.IntegerField(default=0)
    cart = models.ManyToManyField("Item", blank=True)

    def do_payment(self, payment):
        pass

    def add_cart(self, item):
        self.cart.add(item)

    def remove_cart(self, item):
        self.cart.remove(item)
        pass
