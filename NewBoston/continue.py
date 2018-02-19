numberTaken = [3, 2,8,9, 4,12,17  ]

print("here are the number still available")

for n in range(1,20):
    if n in numberTaken:
        continue
    print(n)
