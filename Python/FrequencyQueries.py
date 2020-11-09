
def frequencyQueries(queries):
    collection = {}
    cumOperationThree = []

    for i in range(0, len(queries)):
        operation = queries[i][0]
        numToAdd = queries[i][1]
        if operation == 1:
            if numToAdd in collection.keys():
                collection[numToAdd] += 1
            else:
                collection[numToAdd] = 1
            # print(collection)

        elif operation == 2:
            if numToAdd in collection.keys() and collection[numToAdd] > 0:
                collection[numToAdd] -= 1
            # print(collection)

        elif operation == 3:
            found = False
            for key in collection:
                if numToAdd == collection[key]:
                    cumOperationThree.append(1)
                    found = True
                    break
            if not found:
                cumOperationThree.append(0)

    print(cumOperationThree)
    return cumOperationThree


Query = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5],
         [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]
frequencyQueries(Query)
