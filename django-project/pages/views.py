from django.shortcuts import render

def home(request):
    return render(request,"home.html",{})

def about(request):
    from pages.namer import gaurav
    return render(request,"about.html",{"my_name":gaurav})

def contact(request):
    return render(request,"contact.html",{})

def python(request):
    return render(request,"python.html",{})