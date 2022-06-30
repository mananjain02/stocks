from django.urls import path
from requests import request 
from . import views

urlpatterns = [
    path('', views.StocksView.as_view(), name='allstocks'),
    path('<slug:symbol>', views.GraphView.as_view(), name='graph'),
]