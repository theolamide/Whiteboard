def areFollowingPatterns(strings, patterns):
    count = 0
    countP = 0
    stringPattern = []
    patternsPattern = []
    index = 0
    indexP = 0

    while index < len(strings) - 1:
        if count == 0:
            startingNumber = strings[index]

        if startingNumber != strings[index+1]:
            stringPattern.append(count)
            print(index)
            count = 0
            startingNumber = strings[index+1]
            index += 1
        elif startingNumber == strings[index+1]:
            count += 1
            index += 1

    while indexP < len(patterns) - 1:
        if countP == 0:
            startingNumber = patterns[indexP]

        if startingNumber != patterns[indexP+1]:
            patternsPattern.append(countP)
            print(indexP)
            countP = 0
            startingNumber = patterns[indexP+1]
            indexP += 1
        elif startingNumber == patterns[indexP+1]:
            countP += 1
            indexP += 1

    if stringPattern == patternsPattern:
        print(stringPattern, patternsPattern)
        print("True")
    else:
        print(stringPattern, patternsPattern)
        print("False")


A = ["cat", "dog", "dog"]
B = ["a", "b", "b"]
areFollowingPatterns(A, B)
