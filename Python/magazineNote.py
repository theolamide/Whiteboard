def checkMagazine(magazine, note):
    magazineDict = {}
    noteDict = {}
    sumOfString = 0
    magCount = 0
    noteCount = 0

    if len(note) > len(magazine):
        print("No")
    else:
        for i in range(0, len(magazine)):
            if magazine[i] in magazineDict.keys():
                newKey = magazine[i] + str(magCount)
                magazineDict[newKey] = 1
                magCount += 1
            else:
                magazineDict[magazine[i]] = 1

        for i in range(0, len(note)):
            if note[i] in noteDict.keys():
                newKey = note[i] + str(noteCount)
                noteDict[newKey] = 1
                noteCount += 1
            else:
                noteDict[note[i]] = 1

        for key in noteDict:
            if key in magazineDict.keys():
                sumOfString += 1
            else:
                sumOfString += 0

        if sumOfString == len(note):
            print("Yes")
        else:
            print("No")
