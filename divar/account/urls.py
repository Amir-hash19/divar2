from django.urls import path
from .views import home_view, register_user

urlpatterns = [
    path("", home_view, name="home-view"),
    path("create-user", register_user, name="create-user"),
]
