y={12:2, 9:1, 14:2}
print(sorted(y.items(), key=lambda x: (x[1],x[0]), reverse=True))