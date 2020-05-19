def removeDuplicates(A):
    arrLength = len(A)
    count = 0

    while count < arrLength - 1:
        Deleted = True
        if A[count] == A[count+1] and Deleted:
            del A[count+1]
            arrLength -= 1
            print("count", count, A)
            print("length", arrLength)
            Deleted = True
        else:
            count += 1
            Deleted = False


Arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(Arr)
