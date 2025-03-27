from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserAccount
import json


def home_view(request):
    return HttpResponse("this is home page")



@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_user = UserAccount.objects.create(
            email = data.get("email"),
            name = data.get("name"),
            lastname = data.get("lastname"),
            age = data.get("age")
        )
        return HttpResponse(f"{created_user.id} user created successfully")
