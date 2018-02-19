def insertion_sort(A):
    for i in range(0,len(A)):
        for j in range(i-1,-1,-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    print(A)
    return A
List = [6,6,6,4,3,7]
print(insertion_sort(List))