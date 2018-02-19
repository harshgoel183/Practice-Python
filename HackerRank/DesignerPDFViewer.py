#!/bin/python3

import sys

x = []
h = list(map(int, input().strip().split(' ')))
word = input().strip()
a = len(word)
#print(a,word,h)
#print(ord(word[0]) - 97)
for i in range(len(word)):
        x.append(h[(ord(word[i]) - 97)])
#print(x)
print(max(x) * len(x) * 1)

#stdin
# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
