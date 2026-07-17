from django.urls import path
from . import views

urlpatterns = [
    path('' , views.reg) ,
    path('create/' , views.create , name='create')  
]