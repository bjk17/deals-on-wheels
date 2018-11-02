"""dow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from dow import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/all/manufacturers', views.all_manufacturers_json),
    path('get/all/cars', views.all_cars_json),
    path('get/all/advertisements', views.all_advertisements_json),
    path('admin/', admin.site.urls),
]
