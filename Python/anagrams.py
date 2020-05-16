def makeAnagrams(a, b):
    # Write your code here
    toCheck = {}
    arrOfDeletedChar = []

    for i in range(0, len(a)):
        if a[i] in toCheck.keys():
            toCheck[a[i]][0] += 1
        else:
            toCheck[a[i]] = [1, 0, 0]

    for i in range(0, len(b)):
        if b[i] in toCheck.keys():
            toCheck[b[i]][1] += 1
        else:
            toCheck[b[i]] = [0, 1, 0]

    for key in toCheck:
        toCheck[key][2] = abs(toCheck[key][0] - toCheck[key][1])
        arrOfDeletedChar.append(toCheck[key][2])

    print(toCheck)
    print("sum", sum(arrOfDeletedChar))


a = "aaaagdbeukjafjk"
b = "kafjasjafoaa"

makeAnagrams(a, b)
