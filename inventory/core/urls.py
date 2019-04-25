from django.contrib import admin
from django.urls import path
from core.views import inventory

urlpatterns = [
    path('inventory', inventory),
]
