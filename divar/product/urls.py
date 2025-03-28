from django.urls import path
from .views import HomePageView, create_category

urlpatterns = [
    path("", HomePageView.as_view(), name="home-view"),
    path("/create-category/", create_category, name="create-category"),
    
]
