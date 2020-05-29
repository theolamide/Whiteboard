def maxArrayQueries(n, queries):
    # Write your code here
    # arrToOutput = [0]*n
    # print(arrToOutput)
    # for i in range(0, len(queries)):
    #     startingIndex = queries[i][0] - 1
    #     endingIndex = queries[i][1] - 1
    #     for j in range(int(startingIndex), int(endingIndex)+1):
    #         arrToOutput[j] = arrToOutput[j]+queries[i][2]
    # print(max(arrToOutput))

    aL = n+2
    arrToOutput = [0]*aL
    currentSum = 0
    maximum = 0

    for i in range(0, len(queries)):
        startingIndex = queries[i][0]
        endingIndex = queries[i][1]
        toSum = queries[i][2]
        print(endingIndex, len(arrToOutput), arrToOutput)
        arrToOutput[startingIndex] += toSum
        if endingIndex+1 <= len(arrToOutput):
            arrToOutput[endingIndex+1] -= toSum

    for i in range(0, len(arrToOutput)):
        currentSum = currentSum+arrToOutput[i]
        if currentSum > maximum:
            maximum = currentSum

    print(maximum, arrToOutput)
    return maximum


arr = [[2, 3, 603],
       [1, 1, 286],
       [4, 4, 882]]
maxArrayQueries(4, arr)
