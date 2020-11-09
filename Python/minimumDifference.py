def minimumAbsDifference(arr):
    minDict = {}

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j:
                absDiff = abs(arr[i]-arr[j])
                sortedSubArr = sorted([arr[i], arr[j]])
                if absDiff == 1:
                    print(sortedSubArr)
                #     print(absDiff, [[arr[i], arr[j]]])
                if absDiff in minDict.keys():
                    if sortedSubArr not in minDict[absDiff]:
                        minDict[absDiff].append(sortedSubArr)
                else:
                    minDict[absDiff] = [sortedSubArr]
    # print(minDict)
    minKey = min(minDict)
    print(sorted(minDict[minKey]))


minimumAbsDifference(
    [32, 112, 127, 126, -39, -52, -51, -104, 19, -11, 67, -29, 61])
