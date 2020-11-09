from Array_test import A


def partitionArray(k, numbers):
    # Write your code here
    originalLength = len(numbers)
    arrayOfObjects = []
    outerWhileFlag = True
    reset = 0

    while outerWhileFlag:
        newDict = {}
        # print("51", newDict)
        outerWhileFlag = False
        count = 0
        index = 0
        while count < k and len(numbers) >= 1:
            if index >= len(numbers):
                # Reset the index to avoid out of range
                index = 0
            else:  # index is still within range, so go on
                if numbers[index] in newDict.keys():
                    if index+1 >= len(numbers):
                        reset += 1
                        arrayOfObjects.append(newDict)
                        count = 0
                        outerWhileFlag = True
                        break
                    else:
                        index += 1
                        outerWhileFlag = True
                else:
                    newDict[numbers[index]] = 1
                    count += 1
                    print("-> newDict:", newDict)
                    del numbers[index]
                    outerWhileFlag = True

        if len(newDict) >= 1:
            reset += 1
            arrayOfObjects.append(newDict)
            count = 0
            outerWhileFlag = True

    for i in range(len(arrayOfObjects)):
        if len(arrayOfObjects[i]) != k:
            print("No")
            print("Length of array ->", originalLength)
            return

    print("Yes")
    print("Length of array ->", originalLength)
    # print(arrayOfObjects)
    return


# partitionArray(2, [3, 5, 3, 2])
# partitionArray(1000, [6, 4, 8, 8, 8, 6, 4, 10, 34, 35,
#                       33, 33, 90, 33, 33, 33, 93, 3, 100, 53, 43, 78, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 89, 89, 90, 54, 43, 2, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 9, 4, 8, 2, 7, 54, 87, 34, 75, 85, 98, 23, 85])

# partitionArray(2, A)
# partitionArray(3, A)
# partitionArray(4, A)
partitionArray(5, A)
# partitionArray(6, A)
# partitionArray(7, A)
# partitionArray(8, A)
# partitionArray(9, A)
# partitionArray(11, A)
# partitionArray(12, A)


# Given an array of numbers, you are required to check if it is possible to partition the array into some subsequences of length k each, such that: Each element in the array occurs in exactly one subsequence All the numbers in a subsequence are distinct Elements in the array having the same value must be in different subsequences Is it possible to partition the array satisfying the above conditions? If it is possible, return "Yes", else return "No".
