from django.urls import path 
from . import views

urlpatterns = [
    path('', views.StocksView.as_view()),
]