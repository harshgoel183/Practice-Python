#!/bin/python3

import sys
a = []
max_val = 1
m = 0
def bin_num(n):
    if n >= 2:
        a.append(n%2)
        return(bin_num(n//2))
    else:
        a.append(1)
        return 1

n = int(input().strip())
bin_num(n)
a.reverse()

for i in range(1,len(a)):
    if a[i-1] is 1 and a[i] is 1:
        max_val += 1
        if i is len(a)-1 and m < max_val:
            m = max_val
    elif a[i-1] is 0 and a[i] is 1:
        max_val = 1
    elif a[i-1] is 1 and a[i] is 0:
        if m <= max_val:
            m = max_val
        max_val = 1
    elif a[i-1] is 0 and a[i] is 0:
        max_val = 1


print(m)
#print(a)
print(len(max(bin(int(input().strip()))[2:].split('0'))))
