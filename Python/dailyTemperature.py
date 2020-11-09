from temperatureArray import Temps


def dailyTemperatures(T):
    currIndex = 0
    flag = True
    toReturn = []

    while flag:
        flag = False
        startIndex = currIndex + 1
        for i in range(startIndex, len(T)):
            if T[i] > T[currIndex]:
                indexToPush = i - currIndex
                # print("i:", i, currIndex , ":currIndex","|To push ->", indexToPush)
                toReturn.append(indexToPush)
                currIndex += 1
                flag = True
                break
            elif T[i] <= T[currIndex] and i == len(T)-1:
                # print("i:", i, currIndex , ":currIndex","|To push ->", 0, "here")
                toReturn.append(0)
                currIndex += 1
                flag = True
                break

        if startIndex == len(T):
            toReturn.append(0)
            flag = False

    print(len(toReturn))
    return toReturn


dailyTemperatures(Temps)
