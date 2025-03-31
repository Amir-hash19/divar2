from django.contrib import admin
from product.models import Product, Payment, Category, Order
from .widgets import RichTextEditorWidget
from django.db import models



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "price")
    list_filter = ("price", "date_created")
    search_fields = ("price", "slug")
    fields = (("title", "category"), "description","quantity" , "price")

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
    




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    list_filter = ("title", )
    search_fields = ("title", "slug")
    actions = ("set_slug_to_null", )
    list_per_page = 20



    def set_slug_to_null(self, request, queryset):
        slug_status = queryset.update(slug=None)
        self.message_user(request, "{}Category Slug set to None Successfully!".format(slug_status))


    set_slug_to_null.short_description = "Mark Selected Category Slug set to None" 

        
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "payment", "date_order", "tracking_code")
    list_filter = ("user", "payment", "tracking_code")
    search_fields = ("user", "payment", "tracking_code", "date_order")
    fields = (("user", "total_price") ,"payment", "date_order")
    list_per_page = 30


    def set_totalprice_to_null(self, request, queryset):
        total_price_status = queryset.update(total_price=None)
        self.message_user(request, "{}Order totalprice set to None Successfully!".format(total_price_status))


    set_totalprice_to_null.short_description = "Mark Selected Category Slug set to None" 
    


    
admin.site.register(Payment)
    

