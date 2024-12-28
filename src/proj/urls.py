"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import home_page_view, python_load_home_page, template_home_page
from .views import template_extended_page, login_extended_page
urlpatterns = [
    path('', home_page_view),
    path('template/', template_home_page),
    path('extended/', template_extended_page),
    path('python-load/', python_load_home_page),
    path('login/', login_extended_page),
    path('admin/', admin.site.urls),
]
