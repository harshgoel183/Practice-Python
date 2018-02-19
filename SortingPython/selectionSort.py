def sorting(A):
    for i in range(0,len(A) - 1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i] , A[minIndex] = A[minIndex], A[i]
    return A
List = [6,4,2,7,1]
print(sorting(List))