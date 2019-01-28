from django.shortcuts import render
from .models import ProductType

# Create your views here.

def index(request):
    return render(request, 'tech/index.html')

def techtypes(request):
    type_list = ProductType.objects.all()
    return render(request, 'tech/types.html', {'type_list': type_list})