from django.db import models
from users.models import Customer
from product.models import Item
from payment.models import *

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_keys=True)
    order_date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    username_user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def do_order(self):
        
        pass

    def delete_order(self):
        self.delete()

    def do_payment(self):
        pass