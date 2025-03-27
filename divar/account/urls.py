from django.urls import path
from .views import (home_view, register_user, 
                    delete_user, update_user,
                    get_user)

urlpatterns = [
    path("", home_view, name="home-view"),
    path("create-user/", register_user, name="create-user"),
    path("delete-user/<int:user_id>", delete_user, name="delete-user"),
    path("update-user/<int:user_id>", update_user, name="update-user"),
    path("show-user/<int:user_id>", get_user, name="get-user"),
]
