from django.shortcuts import render
from .models import User

def  reg(request):                                                                                                      
    return render(request , 'users/data_registr.html')

def create(request):
    return render(request , 'users/create.html' ,{'title' : 'Create page'})