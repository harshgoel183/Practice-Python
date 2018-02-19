import heapq

grades = [32, 43, 535, 22, 21, 556, 234]
print(heapq.nlargest(3, grades))# 3 means 3 biggest

stocks = [
    {'ticker': 'AAPL','price': 201},
    {'ticker': 'GOOG','price': 800},
    {'ticker': 'F','price': 54},
    {'ticker': 'MSFT','price': 313},
    {'ticker': 'TUNA','price': 68}
]
print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))
