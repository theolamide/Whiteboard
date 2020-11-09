def longestCommonPrefix(strs):
    freqDictionary = {}
    flag = True
    count = 0
    currentString = ""

    if len(strs) == 1:
        return strs[0]
    elif len(strs) > 1 and len(strs[0]) > 0:
        maxPossibleLength = len(strs[0])
        for i in range(0, len(strs)):
            if len(strs[i]) < maxPossibleLength:
                maxPossibleLength = len(strs[i])

            if len(strs[i]) < 1:
                return currentString

        while flag:
            currentLetter = strs[0][count]
            if currentLetter in freqDictionary.keys():
                freqDictionary[currentLetter] += 1
            else:
                freqDictionary[currentLetter] = 1

            for i in range(1, len(strs)):
                print(i)
                referenceLetter = strs[i][count]
                keyModulo = freqDictionary[currentLetter] % len(strs)
                print(strs[i])

                if referenceLetter == currentLetter and keyModulo != 0:
                    freqDictionary[currentLetter] += 1
                elif referenceLetter != currentLetter and keyModulo != 0:
                    return currentString

            keyModulo = freqDictionary[currentLetter] % len(strs)

            if keyModulo == 0:
                currentString += currentLetter
                if count+1 < maxPossibleLength:
                    count += 1
                else:
                    return currentString
    else:
        return ""


A = ["c", "c"]
longestCommonPrefix(A)
