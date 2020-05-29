def minimumSwaps(arr):
    count = 0
    startingIndex = 0
    flag = True
    print(arr)
    while flag:
        # print("startingIndex", startingIndex)
        flag = False
        for i in range(int(startingIndex), len(arr)-1):
            if arr[i] != i+1:
                startingIndex = i
                firstNumFlag = True
                break

        for j in range(int(startingIndex), len(arr)):
            if arr[j] == startingIndex+1:
                secNum = arr[j]
                secNumFlag = True
                break

        if firstNumFlag and secNumFlag:
            hold = secNum
            arr[j] = arr[i]
            arr[i] = hold
            count += 1
            firstNumFlag = False
            secNumFlag = False
            flag = True
            print(arr)

    print(arr)
    print("count", count)
    return count


# arr3 = [1, 2, 5, 3, 7, 8, 6, 4]
# arr3 = [7, 1, 3, 2, 4, 5, 6]
# # arr3 = [4, 3, 1, 2]
# minimumSwaps(arr3)

# create dictionary of element and current index
# Element 1, in Index 2
# {
#     1: 1,
#     2: 0,
#     3: 1,
#     4: 4,
#     5: 5,
#     6: 6,
#     7: 0
# }

# {
#     1: 1,
#     0: 2
# }


def minimumSwapsDictionary(arr):
    valueToCurrentIndex = {}
    indexToCurrentFilled = {}
    count = 0

    for i in range(0, len(arr)):
        valueToCurrentIndex[arr[i]] = i
        indexToCurrentFilled[i] = arr[i]

    print(valueToCurrentIndex)
    orderedKeys = sorted(valueToCurrentIndex.keys())
    for element in orderedKeys:
        rightIndex = element-1
        # checking to see if I'm in the right position
        if valueToCurrentIndex[element] != rightIndex:
            # If not, check other dictionary to see who is in my index and grab my index from them
            whoIsInMyCorrectIndexPosition = indexToCurrentFilled[rightIndex]
            myPreferredIndex = valueToCurrentIndex[whoIsInMyCorrectIndexPosition]
            # SWAP
            # Give my current index to some to hold
            # Get my correct index
            # Give my old index "currentindex" to the person who had my correct index
            myCurrentIndex = valueToCurrentIndex[element]
            valueToCurrentIndex[element] = myPreferredIndex
            valueToCurrentIndex[whoIsInMyCorrectIndexPosition] = myCurrentIndex
            # Update the SWAP in the index dictionary
            indexToCurrentFilled[rightIndex] = element
            indexToCurrentFilled[myCurrentIndex] = whoIsInMyCorrectIndexPosition
            count += 1
            # print(valueToCurrentIndex)

    print(valueToCurrentIndex)
    print(count)


arr3 = [7, 1, 3, 2, 4, 5, 6]
# arr3 = [4, 3, 1, 2]
minimumSwapsDictionary(arr3)
