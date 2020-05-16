def removeDuplicates(A):
    for i in range(0, len(A)-1):
        L = len(A)
        print(i, L)
        if A[i] == A[i+1]:
            del A[i+1]
            # print(i, A[i], A)
    print(A)


Arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(Arr)
