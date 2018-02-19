#!/bin/python3
import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
b = [int(a_temp) for a_temp in input().strip().split(' ')]
result = []
for m in range(q):
    m = int(input())
    result.append(b[m-k % n])
for e in result:
    print(e)
