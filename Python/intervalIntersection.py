

def intervalIntersection(A, B):
    aIndex = 0
    bIndex = 0
    toReturn = []
    arg1 = A[aIndex]
    arg2 = B[bIndex]
    flag = True

    def compareArrs(aArr, bArr):
        signifyInd = ""
        zipComp = zip(aArr, bArr)
        compList = list(zipComp)
        lowIntSec = max(compList[0])
        highIntSec = min(compList[1])

        if aArr[0] > bArr[1]:
            signifyInd = "B"
            intersection = "NO INTERSECTION"
        elif bArr[0] > aArr[1]:
            signifyInd = "A"
            intersection = "NO INTERSECTION"
        else:
            if aArr[1] == highIntSec:
                signifyInd = "A"
            elif bArr[1] == highIntSec:
                signifyInd = "B"

            intersection = [lowIntSec, highIntSec]

        return [intersection, signifyInd]

    while flag:
        arg1 = A[aIndex]
        arg2 = B[bIndex]
        flag = False
        result = compareArrs(arg1, arg2)
        print(result)
        if result[0] == "NO INTERSECTION":
            pass
        else:
            toReturn.append(result[0])

        if result[1] == "A":
            if aIndex == len(A)-1:
                print(toReturn)
                return toReturn
            else:
                aIndex += 1
                print("aIndex", aIndex)
                flag = True

        elif result[1] == "B":
            if bIndex == len(B)-1:
                print(toReturn)
                return toReturn
            else:
                bIndex += 1
                print("bIndex", bIndex)
                flag = True

    return toReturn


A = [[0, 2], [5, 10], [13, 23], [24, 25]]

B = [[1, 5], [8, 12], [15, 24], [25, 26]]


intervalIntersection(A, B)
