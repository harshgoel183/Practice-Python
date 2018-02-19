stocks = {
    'AAPL': 201,
    'GOOG': 55 ,
    'F':54,
    'MSFT': 313,
    'TUNA': 68}
#print(min(stocks))

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
