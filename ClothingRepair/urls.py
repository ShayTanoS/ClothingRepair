"""
URL configuration for ClothingRepair project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from loginapp import urls as loginapp_urls
from clientapp import urls as clientapp_urls
from employeesapp import urls as employeesapp_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include(loginapp_urls)),
    path('', include(clientapp_urls)),
    path('employees/', include(employeesapp_urls)),
]
