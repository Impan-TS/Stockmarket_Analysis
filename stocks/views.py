from django.shortcuts import render
from yahoo_fin.stock_info import *

# Create your views here.
def home(request):
    stock_list = tickers_nifty50()
    
    new_stocks = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BPCL.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 
            'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INFY.NS', 'JSWSTEEL.NS',
            'POWERGRID.NS', 'SBIN.NS', 'SBILIFE.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS', 'UPL.NS']
    
    update_stock = stock_list.index('MM.NS')
    stock_list[update_stock] = 'M&M.NS'
    
    stock_list.extend(new_stocks)
    stock_list.sort()

    return render(request, 'stocks/index.html', {'stock_list':stock_list})

def stocksInfo(request):
    stock_list = request.GET.getlist('stock_list')
    request.session.create()
    stock_details = {}
    for stock in stock_list:
        stock_detail = get_quote_table(stock)
        stock_details.update({stock:stock_detail})
    return render(request, 'stocks/selectedstocks.html', {'stock_details':stock_details})
