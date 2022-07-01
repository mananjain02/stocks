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
        for i in request.POST['symbol'].upper():
            if not (i>='A' and i<='Z'):
                return HttpResponseRedirect(reverse('allstocks'))
        stock = StockList()
        stock.name = request.POST['name']
        stock.symbol = request.POST['symbol'].upper()
        stock.user = request.user
        stock.save()
        redirect_path = reverse('allstocks')
        return HttpResponseRedirect(redirect_path)

