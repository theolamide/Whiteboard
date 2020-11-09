
def longestSubstring(s):
    string = ""
    lengths = []
    count = 0
    indexToStart = 0
    print("input string length", len(s))

    if len(s) == 0:
        return 0

    while count <= len(s):
        count += 1
        for i in range(indexToStart, len(s)):
            whiteSpace = False
            if s[i].isspace() == True:
                whiteSpace = True

            if whiteSpace:
                replacementString = "@"
                print(len(string), string, "string")
                if replacementString in string:
                    lengths.append(len(string))
                    indexToStart = i+1
                    string = replacementString
                    break
                elif count == len(s):
                    string += replacementString
                    lengths.append(len(string))
                else:
                    string += replacementString
                    print(string)
            else:
                if s[i] in string:
                    lengths.append(len(string))
                    indexToStart = i+1
                    string = s[i]
                    break
                elif count == len(s):
                    string += s[i]
                    lengths.append(len(string))
                else:
                    string += s[i]
                    print(string)

    if len(lengths) == 0:
        return 0
    else:
        print("max", max(lengths))
        return max(lengths)


string = "dvdf"
longestSubstring(string)
