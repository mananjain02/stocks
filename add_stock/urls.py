from django.urls import path 
from . import views

urlpatterns = [
    path('', views.AddStockView.as_view(), name="addstock")
]