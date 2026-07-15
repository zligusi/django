from django.shortcuts import render
from .models import User

def  register(request):
    user = User.objects.all()                                                                                                       
    return render(request , 'users/registr.html' , {'user': user})