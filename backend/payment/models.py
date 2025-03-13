from django.db import models

# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    payment_method_id = models.IntegerField()

    def get_payment_method(self):
        return self.payment_method_id()
    
    def pay(self):
        pass

class Ewallet(Payment):
    money = models.IntegerField()

    def get_money(self):
        return self.money()
    
class CreditCard(Payment):
    card_no = models.IntegerField()
    cvv = models.IntegerField()
    card_provider = models.CharField()

    def get_card_no(self):
        return self.card_no
    
    def get_cvv(self):
        return self.cvv
    
    def get_card_provider(self):
        return self.card_provider
    

class DebitCard(Payment):
    card_no = models.IntegerField()
    account = models.IntegerField()
    bank = models.CharField()
    money = models.IntegerField()

    def get_account(self):
        return self.account
    
    def get_money(self):
        return self.money
    
    