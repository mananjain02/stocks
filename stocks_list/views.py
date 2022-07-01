from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import StockList
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Create your views here.
class StocksView(View):
    def get(self, request):
        if(request.user.is_authenticated):
            stocks = StockList.objects.filter(user=request.user)
            context = {
                'stocks': stocks
            }
            return render(request, 'stocks_list/stockslist.html', context)
        else:
            return HttpResponseRedirect('accounts/login')

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

class GraphView(View):
    def get(self, request, symbol):
        try:
            api_key = 'C7UWME84WXZD1O26'
            period = 60
            ts = TimeSeries(key=api_key, output_format='pandas')
            data_ts = ts.get_intraday(symbol.upper(), interval="1min", outputsize='full')
            # ti = TechIndicators(key=api_key, output_format="pandas")
            # data_ti, meta_data_ti = ti.get_rsi(symbol.upper(), interval="1min", time_period=period, series_type="close")
            df = data_ts[0][period::]
            # df2 = data_ti
            # total_data = pd.concat([df,df2], axis=1, sort=True)
            plt.switch_backend('AGG')
            plt.plot(df['4. close'])
            plt.title(symbol)
            plt.ylabel('price')
            plt.xlabel('time')
            # plt.savefig("graph.png", format="png")
            stocks = StockList.objects.filter(user=request.user)
            graph = get_graph()
            context = {
                'stocks': stocks,
                'graph': graph
            }
            return render(request, 'stocks_list/stockslist.html', context)
        except:
            return HttpResponseRedirect(reverse('allstocks'))