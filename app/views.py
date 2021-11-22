from django.shortcuts import render

# Create your views here.

def Registration(request):
    return render(request,'h1.html')

def online_Form(request):
    return render(request,'h2.html')    