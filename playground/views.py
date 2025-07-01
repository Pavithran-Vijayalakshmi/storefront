from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Hello World")

def Maths(request):
    return HttpResponse("I love Mathematics")

def html(request):
    return render(request, 'welcome.html')

