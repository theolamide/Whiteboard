def leftRotation(a, d):
    count = 0

    while count < d:
        firstElement = a[0]
        del a[0]
        a.append(firstElement)
        count += 1
        print(a)


arr = [1, 2, 3, 4, 5]
leftRotation(arr, 4)
