# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def addMin(arr):
    toSum = []

    for i in range(0, len(arr)):
        toSum.append(min(arr[i]))
        # print(i)

    print(sum(toSum))


addMin([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])
