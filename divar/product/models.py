from django.db import models
from account.models import UserAccount



class Product(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    quantity = models.IntegerField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title}"




class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=1560, unique=True)


    def __str__(self):
        return f"{self.title}"



class Order(models.Model):
    user = models.ForeignKey(to=UserAccount, on_delete=models.CASCADE,null=True, related_name="useraccount")
    payment = models.ForeignKey(to="Payment", on_delete=models.SET_NULL, null=True, blank=True, related_name="payment")
    total_price = models.FloatField(blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=200, null=True,blank=True)

    
    def __str__(self):
        return f"{self.user.name}"
    


class Payment(models.Model):
    user = models.ForeignKey(to=UserAccount, on_delete=models.CASCADE)
    payment_number = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_number}"
