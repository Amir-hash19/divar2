from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json



class HomePageView(TemplateView):
    template_name = "home.html"




@csrf_exempt
def create_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_category = Category.objects.create(
            title = data.get("title"),
            slug = data.get("slug"),
        )
        return HttpResponse(f"{created_category.id} Category created successfully")
        
