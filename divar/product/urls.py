from django.urls import path
from .views import (HomePageView, create_category,
                     create_product, delete_product, 
                     delete_category, display_product,
                       display_category, update_product, update_category)

urlpatterns = [
    path("", HomePageView.as_view(), name="home-view"),
    path("/create-category/", create_category, name="create-category"),
    path("/create-product/", create_product, name="create-product"),
    path("/delete-product/<int:product_id>", delete_product, name="delete-product"),
    path("/delete-category/<int:category_id>", delete_category, name="delete-category"),
    path("/display-product/<int:product_id>", display_product, name="display-product"),
    path("/display-category/<int:category_id>", display_category, name="display-category"),
    path("/update-product/<int:product_id>", update_product, name="update-product"),
    path("/update-category/<int:category_id>", update_category, name="update-category"),
    
]
