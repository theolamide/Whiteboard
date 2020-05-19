
def frequencyQueries(queries):
    collection = {}
    freqCollection = {}
    threeOutput = []

    for i in range(0, len(queries)):
        operation = queries[i][0]
        if operation == 1:
            if queries[i][1] in collection.keys():
                collection[queries[i][1]] += 1
                toPutInFreq = collection[queries[i][1]] - 1
                if toPutInFreq in freqCollection.keys() and freqCollection[toPutInFreq] == queries[i][1]:
                    freqCollection[collection[queries[i][1]]
                                   ] = freqCollection.pop(toPutInFreq)
                print(i, collection)
            else:
                collection[queries[i][1]] = 1
                freqCollection[1] = queries[i][1]
                print(i, collection)

        elif operation == 2:
            if queries[i][1] in collection.keys() and collection[queries[i][1]] > 0:
                if collection[queries[i][1]] in freqCollection.keys() and freqCollection[toPutInFreq] == queries[i][1]:
                    freqCollection[collection[queries[i][1]] -
                                   1] = freqCollection.pop(toPutInFreq)
                collection[queries[i][1]] -= 1
                print(i, collection)

        elif operation == 3:
            if queries[i][1] in freqCollection.keys():
                threeOutput.append(1)
            else:
                threeOutput.append(0)

    print(threeOutput)
    return threeOutput


Query = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
frequencyQueries(Query)
