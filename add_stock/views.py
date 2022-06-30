from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from stocks_list.models import StockList

# Create your views here.
class AddStock(View):
    def get(self, request):
        return render(request, 'add_stock/add-stock.html')

    def post(self, request):
        stock = StockList()
        stock.name = request.POST['name']
        stock.symbol = request.POST['symbol']
        stock.user = request.user
        stock.save()
        redirect_path = reverse('allstocks')
        return HttpResponseRedirect(redirect_path)

