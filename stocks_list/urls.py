from django.urls import path, include
from requests import request 
from . import views

urlpatterns = [
    path('', views.StocksView.as_view(), name='allstocks'),
    path('add-stock/', include('add_stock.urls')),
    path('remove-stock/', include('remove_stock.urls')),
    path('accounts/', include('allauth.urls')),
    path('<slug:symbol>/<slug:inter>', views.GraphView.as_view(), name='graph')
]