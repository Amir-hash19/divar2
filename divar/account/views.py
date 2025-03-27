from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserAccount
from django.shortcuts import get_object_or_404
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



@csrf_exempt
def delete_user(request, user_id):
    if request.method == "DELETE":
        user = get_object_or_404(UserAccount, id=user_id)
        user.delete()
        return HttpResponse("The user deleted successfully")
        
    

@csrf_exempt
def update_user(request, user_id):
    try:
        user = UserAccount.objects.get(id=user_id)
    except UserAccount.DoesNotExist:
        return JsonResponse({"error":"User not found"}, status=404)
    
    if request.method in ["PUT","PATCH"]:
        data = json.loads(request.body)
        if request.method == "PUT":
            user.email = data.get("email", user.email)
            user.name = data.get("name", user.name)
            user.lastname = data.get("lastname", user.lastname)
            user.age = data.get("age", user.age)

        elif request.method == "PATCH":
            if "email" in data:
                user.email = data["email"]
            if "name" in data:
                user.name = data["name"]
            if "lastname" in data:
                user.lastname = data["lastname"]
            if "age" in data:
                user.age = data["age"]        
        user.save()
        return HttpResponse("The user updated successfully!")
              

@csrf_exempt
def get_user(request, user_id):
    try:
        user = UserAccount.objects.get(id=user_id)
        user_data = {
            "id":user.id,
            "email":user.email,
            "name":user.name,
            "lastname":user.lastname,
            "age":user.age
        }  
        return JsonResponse(user_data)
    except UserAccount.DoesNotExist:
        return JsonResponse({"error":"User not found"}, status=404)

                


    
        
          


    

