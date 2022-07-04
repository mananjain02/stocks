from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from stocks_list.models import StockList
from add_stock.models import AllStocks

# Create your views here.
class AddStockView(View):
    def get(self, request):
        all_stocks = AllStocks.objects.all()
        already_added_stocks = StockList.objects.filter(user=request.user)
        already_added_stocks_name = []
        stocks_to_show_to_add = []
        for stock in already_added_stocks:
            already_added_stocks_name.append(stock.name)
        
        for stock in all_stocks:
            if stock.name not in already_added_stocks_name:
                stocks_to_show_to_add.append(stock)

        context = {
            "all_stocks": stocks_to_show_to_add,
        }
        return render(request, 'add_stock/add-stock.html', context)

    def post(self, request):
        stock_to_add = StockList(
            name = request.POST['name'],
            symbol = request.POST['symbol'],
            user = request.user,
        )
        stock_to_add.save()
        return HttpResponseRedirect(reverse('addstock'))

