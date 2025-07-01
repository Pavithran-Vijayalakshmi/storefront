from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.sayHello),
    path('math/',views.Maths),
    path('html/',views.html),
    path('',views.sayHello),
] 