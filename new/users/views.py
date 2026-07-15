from django.shortcuts import render
from .models import User

def  reg(request):                                                                                                      
    return render(request , 'users/reg.html')