def removeDuplicates(A):
    arrLength = len(A)
    count = 0

    while count < arrLength - 1:
        if A[count] == A[count+1]:
            del A[count+1]
            arrLength -= 1
            print("count", count, A)
            print("length", arrLength)
        else:
            count += 1


Arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(Arr)
