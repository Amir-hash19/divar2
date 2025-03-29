from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
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
        




@csrf_exempt
def create_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            category_id = data.get("category_id")
            if not category_id:
                return JsonResponse({"error": "category_id is required"}, status=400)

            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:  
                return JsonResponse({"error": "category not found"}, status=404)

            created_product = Product.objects.create(
                title=data.get("title"),
                price=data.get("price"),
                description=data.get("description"),
                slug=data.get("slug"),
                quantity=data.get("quantity"),
                category=category,  
            )

            return JsonResponse({"message": f"Product with ID {created_product.id} was created successfully!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

        


@csrf_exempt
def delete_product(request, product_id):
    if request.method == "DELETE":
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return HttpResponse("the product was deleted successfully!")


    

@csrf_exempt
def delete_category(request, category_id):
    if request.method == "DELETE":
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return HttpResponse("the category was deleted successfully!")





@csrf_exempt
def display_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product_data = {
            "id":product.id,
            "title": product.title,
            "price": product.price,
            "description": product.description,
            "slug": product.slug,
            "quantity": product.quantity,
            "category":product.category.id
        }
        return JsonResponse(product_data, safe=True)
    except Product.DoesNotExist:
        return JsonResponse({"error":"User not found"})



@csrf_exempt
def display_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        category_data = {
            "title":category.title,
            "slug":category.slug,
        }
        return JsonResponse(category_data, safe=True)
    except Category.DoesNotExist:
        return JsonResponse({"error":"Category not found!"})





@csrf_exempt
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        try:
            if request.method == "PUT":
                product.title = data.get("title", product.title)
                product.price = float(data.get("price", product.price))  
                product.description = data.get("description", product.description)
                product.slug = data.get("slug", product.slug)
                product.quantity = int(data.get("quantity", product.quantity)) 

                if "category" in data:
                    product.category = Category.objects.get(id=int(data["category"])) 
            elif request.method == "PATCH":
                if "title" in data:
                    product.title = data["title"]
                if "price" in data:
                    product.price = float(data["price"])
                if "description" in data:
                    product.description = data["description"]
                if "slug" in data:
                    product.slug = data["slug"]
                if "quantity" in data:
                    product.quantity = int(data["quantity"])
                if "category" in data:
                    product.category = Category.objects.get(id=int(data["category"]))

            product.save()
            return JsonResponse({"message": "The product updated successfully!"}, status=200)
        except ValueError:
            return JsonResponse({"error": "Invalid data type in request"}, status=400)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)






@csrf_exempt
def update_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=404)

    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        if request.method == "PUT":
            category.title = data.get("title", category.title)
            category.slug = data.get("slug", category.slug)
        elif request.method == "PATCH":
            if "title" in data:
                category.title = data["title"]
            if "slug" in data:
                category.slug = data["slug"]

        category.save()
        return JsonResponse({"message": "The category updated successfully"}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)





                

        

    



    
