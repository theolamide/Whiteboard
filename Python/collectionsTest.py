from collections import Counter


def objectCounter(arr):
    freqObject = Counter(arr)
    regularDict = dict(freqObject)

    print(regularDict)


A = [6, 4, 8, 8, 8, 6, 4, 10, 34, 35, 33, 33, 90, 33, 33, 33, 93, 3, 100, 53, 43, 78, 23, 23, 23, 23, 23, 23, 23, 23, 23,
     23, 23, 23, 23, 23, 89, 89, 90, 54, 43, 2, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 9, 4, 8, 2, 7, 54, 87, 34, 75, 85, 98, 23, 85]

objectCounter(A)
