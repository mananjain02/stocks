from django.urls import path 
from . import views

urlpatterns = [
    path('', views.RemoveStockView.as_view(), name="removestock")
]