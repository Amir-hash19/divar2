from django.contrib import admin
from product.models import Product, Payment, Category, Order
from .widgets import RichTextEditorWidget
from django.db import models



class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "price")
    list_filter = ("price", "date_created")
    search_fields = ("price", "slug")
    fields = (("title", "price"), "description","quantity" , "category")

    formfield_overrides = {
        models.TextField: {"widget": RichTextEditorWidget},  
    }


    @admin.display(empty_value="???")
    def view_date_created(self, obj):
        return obj.date_created.strftime("%Y-%M-%D") if obj.date_created else "???"
    

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("title", "price")
        return ("slug", "date_created")
    
    
admin.site.register(Product, ProductAdmin)
    

