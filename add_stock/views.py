from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from stocks_list.models import StockList
from add_stock.models import AllStocks

# Create your views here.
class AddStockView(View):
    def get(self, request):
        all_stocks = AllStocks.objects.all()
        context = {
            "all_stocks": all_stocks
        }
        return render(request, 'add_stock/add-stock.html', context)

    def post(self, request):
        all_stocks = StockList.objects.all()
        for stock in all_stocks:
            if stock.symbol == request.POST['symbol']:
                return render(request, 'add_stock/add-stock.html', {
                    "error_message": f"{ stock.name } is already added",
                    "all_stocks": AllStocks.objects.all()
                })
        stock_to_add = StockList(
            name = request.POST['name'],
            symbol = request.POST['symbol'],
            user = request.user
        )
        stock_to_add.save()
        return HttpResponseRedirect(reverse('addstock'))

