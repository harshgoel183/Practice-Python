def sortings(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A

print(sortings([4,3,6,2,7]))