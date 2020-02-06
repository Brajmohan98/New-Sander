from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index-02.html")
def careers(request):
    return render(request, "careers.html")
def login_register(request):
    return render(request, "login-register.html")
def aboutus(request):
    return render(request, "about-us.html")
def shop(request):
    return render(request, "shop.html")
def single_product(request):
    return render(request, "single-product.html")
def single_project(request):
    return render(request, "single-project.html")
def our_projects(request):
    return  render(request, "our-projects.html")



def login(request):
    return HttpResponse("Hello")