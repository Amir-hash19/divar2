from django.contrib import admin
from product.models import Product, Order, Payment, Category


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
