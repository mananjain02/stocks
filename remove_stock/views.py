from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from stocks_list.models import StockList
from django.urls import reverse

# Create your views here.
class RemoveStockView(View):
    def get(self, request):
        all_stocks = StockList.objects.filter(user=request.user)
        error_message = ""
        if len(all_stocks) is 0:
            error_message = "No stocks added"
        context = {
            "all_stocks": all_stocks,
            "error_message": error_message,
        }
        return render(request, 'remove_stock/remove-stock.html', context)

    def post(self, request):
        # Need to use the method to run multiple filters at one time
        obj = StockList.objects.filter(name=request.POST['name'])
        obj1 = obj.filter(user=request.user)
        obj1.delete()
        all_stocks = StockList.objects.filter(user=request.user)
        error_message = ""
        if len(all_stocks) is 0:
            error_message = "No stocks added"
        context = {
            "all_stocks": all_stocks,
            "error_message": error_message,
        }
        return render(request, 'remove_stock/remove-stock.html', context)