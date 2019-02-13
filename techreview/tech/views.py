from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product

# Create your views here.

def index(request):
    return render(request, 'tech/index.html')

def techtypes(request):
    type_list = ProductType.objects.all()
    return render(request, 'tech/types.html', {'type_list': type_list})

def getproducts(request):
    product_list = Product.objects.all()
    return render(request, 'tech/products.html', {'product_list': product_list})

def productdetail(request, id):
    detail = get_object_or_404(Product, pk=id)
    return render(request, 'tech/details.html', {'detail': detail})
