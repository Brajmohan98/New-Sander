"""sanders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sanders_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('careers',views.careers),
    path('signup',views.login_register),
    path('aboutus',views.aboutus),
    path('shop',views.shop),
    path('single-product',views.single_product),
    path('single-project',views.single_project),
    path('our-projects',views.our_projects),
    path('login',views.login),
]
