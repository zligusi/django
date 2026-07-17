from django.shortcuts import render

def index(request):  
    return render(request , 'main/index.html' ,{'title' : 'Home page'})

def about(request):
    return render(request , 'main/about.html' ,{'title' : 'About page'})

def create(request):
    return render(request , 'users/create.html' ,{'title' : 'Create page'})