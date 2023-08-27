from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Product,Category,Fabricant

# Create your views here.
def product_list(request):
    return render(request,"products/index.html")


def category_list(request):
    return HttpResponse("Criamos uma nova categoria")



def product_new(request):
    category = Category.objects.first()
    fabricant = Fabricant.objects.first()
    try:
        Product.objects.create(name='Shirt Mullin',price=39.99,
                                qtd=22,date_created="",date_updated="",
                                url="url-mullin-shirt",is_active=True,category=category,fabricant=fabricant)
    except IntegrityError:
        return HttpResponse("Sorry somethings is going wrong!")    
    return HttpResponse("Product screen to create a new")
