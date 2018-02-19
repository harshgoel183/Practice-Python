marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
print(marksheet)
# a = set([marks for name, marks in marksheet])
# print(a)
# b = list(set([marks for name, marks in marksheet]))
# print(b)
c = sorted(set([marks for name, marks in marksheet]))[1]
print(c)
print('\n'.join([a for a,b in sorted(marksheet) if b == c]))
