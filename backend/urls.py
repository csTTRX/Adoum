"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('atuim270/', admin.site.urls),
    path('', home, name = 'home'),
    path('add-formation/', add_formation, name = 'add_formation'),
    path('add-experience/', add_experience, name = 'add_experience'),
    path('add-formation/<int:id>', del_formation, name = 'del_formation'),
    path('add-experience/<int:id>', del_experience, name = 'del_experience'),
]
