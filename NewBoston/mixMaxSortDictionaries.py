stocks = {
    'GOOG' : 520.54,
    'FB' : 76.3,
    'YHOO':33.5,
    'AMZN':303.3,
    'AAPL':99.4
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

print(min(zip(stocks.keys(), stocks.values())))
print(max(zip(stocks.keys(), stocks.values())))
print(sorted(zip(stocks.keys(), stocks.values())))
