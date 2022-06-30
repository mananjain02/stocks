from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import StockList
import alpha_vantage

# Create your views here.
class StocksView(View):
    def get(self, request):
        stocks = StockList.objects.filter(user=request.user)
        print(stocks)
        return HttpResponse('found')
