import array

arr = array.array('i',[1,2,4])

for i in arr:
    print(i)

arr.pop(2)

for i in arr:
    print(i)

arr.append(1)
arr.append(5)
arr.append(8)

arr.remove(1)
print("-----------------")
for i in arr:
    print(i)