from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'about.html')

def blogs(request):
    return render(request,'blogs.html')

def f1(request):
    return render(request,'blogs/1.html')

def f2(request):
    return render(request,'blogs/2.html')