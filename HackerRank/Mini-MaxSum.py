#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
l=[a,b,c,d,e]
x = sum(l)
print(x-max(l),x-min(l))

# Input (stdin)
# 1 2 3 4 5
