"""work_registration_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from work_registry.views import list_registry, add_registry, \
                                delete_registry,confirm_registry,homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('add-registry/', add_registry, name="add-registry"),
    path('list-registry/', list_registry, name="list-registry"),
    path('confirm-registry/<int:pk>', confirm_registry, name="confirm-registry"),
    path('delete-registry/<int:pk>/', delete_registry, name="delete-registry"),
]
