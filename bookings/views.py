from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(request,'bookings/home.html')

def view(request):
    product = Product.objects.all()
    return render(request,'bookings/product.html',{'products': product})

