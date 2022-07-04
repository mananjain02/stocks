from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import StockList
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import threading
import time

# Create your views here.
time_slots = ['1min', '5min', '15min', '30min', '60min']
api_key = 'C7UWME84WXZD1O26'
period = 60
data = {}


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


class ApiDataFetch(threading.Thread):
    def __init__(self, symbols):
        self.symbols = symbols
        threading.Thread.__init__(self)

    def run(self):
        for symbol in self.symbols:
            time_interval_vs_graph = {}
            for inter in time_slots:
                if data.get(symbol) is None or data.get(symbol).get(inter) is None:
                    # ts = TimeSeries(key=api_key, output_format='pandas')
                    # data_ts = ts.get_intraday(symbol, interval=inter, outputsize='full')
                    # # ti = TechIndicators(key=api_key, output_format="pandas")
                    # # data_ti, meta_data_ti = ti.get_rsi(symbol.upper(), interval="1min", time_period=period, series_type="close")
                    # df = data_ts[0][period::]
                    # # df2 = data_ti
                    # # total_data = pd.concat([df,df2], axis=1, sort=True)
                    # plt.switch_backend('AGG')
                    # plt.plot(df['4. close'])
                    # plt.title(symbol)
                    # plt.ylabel('price')
                    # plt.xlabel('time')
                    # plt.title(symbol)
                    # graph = get_graph()
                    time_interval_vs_graph[inter] = symbol+inter
                    # for company in data:
                    #     for interval in company:
                    #         print(company, interval.key())
                    print(symbol, inter)
                    time.sleep(10)
            data[symbol] = time_interval_vs_graph


class StocksView(View):
    def get(self, request):
        if(request.user.is_authenticated):
            stocks = StockList.objects.filter(user=request.user)
            stocks_symbol = []
            for stock in stocks:
                stocks_symbol.append(stock.symbol.upper())
            ApiDataFetch(stocks_symbol).start()
            context = {
                'stocks': stocks,
                'interval_time': time_slots[0]
            }
            return render(request, 'stocks_list/stockslist.html', context)
        else:
            return HttpResponseRedirect(reverse('account_login'))


class GraphView(View):
    def get(self, request, symbol, inter):
        try:
            if data.get(symbol.upper()) is None or data.get(symbol.upper()).get(inter) is None:
                # ts = TimeSeries(key=api_key, output_format='pandas')
                # data_ts = ts.get_intraday(
                #     symbol.upper(), interval=inter, outputsize='full')
                # # ti = TechIndicators(key=api_key, output_format="pandas")
                # # data_ti, meta_data_ti = ti.get_rsi(symbol.upper(), interval="1min", time_period=period, series_type="close")
                # df = data_ts[0][period::]
                # # df2 = data_ti
                # # total_data = pd.concat([df,df2], axis=1, sort=True)
                # plt.switch_backend('AGG')
                # plt.plot(df['4. close'])
                # plt.title(symbol)
                # plt.ylabel('price')
                # plt.xlabel('time')
                # plt.title(symbol)
                # # plt.savefig("graph.png", format="png")
                # stocks = StockList.objects.filter(user=request.user)
                # graph = get_graph()
                data[symbol][inter] = symbol+inter
                graph = data[symbol][inter]
                context = {
                    'stocks': stocks,
                    'graph': graph,
                    'time_slots': time_slots,
                    'symbol': symbol,
                    'interval_time': inter
                }
                return render(request, 'stocks_list/stockslist.html', context)
            else:
                print("found in dictionary")
                stocks = StockList.objects.filter(user=request.user)
                context = {
                    'stocks': stocks,
                    'graph': data[symbol][inter],
                    'time_slots': time_slots,
                    'symbol': symbol,
                    'interval_time': inter
                }
                return render(request, 'stocks_list/stockslist.html', context)
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse('allstocks'))
