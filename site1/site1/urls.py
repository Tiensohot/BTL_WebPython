from django.contrib import admin
from django.urls import path, include
from my_app import views as home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home.home)
]
