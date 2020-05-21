def twoDimensional(arr):
    sumCollection = []

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[i])-2):
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            singleSum = a+b+c+d+e+f+g
            sumCollection.append(singleSum)
            print(a, b, c)
            print(" ", d)
            print(e, f, g)
            print("")

    print(max(sumCollection))


twoDArray = [[9, 9, 9, 1, 1, 1],
             [0, 9, 0, 4, 3, 2],
             [9, 9, 9, 1, 2, 3],
             [0, 0, 8, 6, 6, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 1, 2, 4, 0]]

twoDimensional(twoDArray)
