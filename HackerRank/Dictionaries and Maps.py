#!/bin/python3

import sys
diction = {}
arr = []
n = int(input().strip())
a = ""
for i in range(0,n):
    arr = [arr_temp for arr_temp in input().strip().split(' ')]
    diction[arr[0]] = arr[1]

new_arr = [new_arr_temp for new_arr_temp in sys.stdin.read().strip().split('\n') ]#sys.stdin.read() reads till EOF
#print(new_arr)

for i in range(0,len(new_arr)):
    a = new_arr[i]
    if a in diction.keys():
        print(a+"="+diction[a])
    else:
        print("Not found")
