from django.urls import path 
from . import views

urlpatterns = [
    path('', views.AddStock.as_view(), name="addstock")
]