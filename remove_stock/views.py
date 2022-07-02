from django.shortcuts import render
from django.views import View
from stocks_list.models import StockList

# Create your views here.
class RemoveStockView(View):
    def get(self, request):
        all_stocks = StockList.objects.filter(user=request.user)
        context = {
            "all_stocks": all_stocks
        }
        return render(request, 'remove_stock/remove-stock.html', context)

    def post(self, request):
        # Need to add filter to filter the user 
        obj = StockList.objects.filter(name=request.POST['name'])
        obj.delete()
        all_stocks = StockList.objects.all()
        context = {
            "all_stocks": all_stocks
        }
        return render(request, 'remove_stock/remove-stock.html', context)