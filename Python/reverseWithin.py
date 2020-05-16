def reverseInParentheses(s):
    # Write your code here
    toReturn = []
    # stack = []
    word = ""
    concatWord = ""

    for i in range(0, len(s)):
        if s[i] != "(" and s[i] != ")":
            word += s[i]

        if s[i] == "(":
            toReturn.append(word)
            word = ""

        if s[i] == ")":
            toReturn.append(reverseString(word))
            word = ""

    for i in range(0, len(toReturn)):
        concatWord += toReturn[i]

    print("word", word)
    print("toReturn", toReturn)
    print("Concat", concatWord)


def reverseStringObj(string):
    newObj = {}

    word = ""
    Key = 1
    closed = 0

    for i in range(0, len(string)):
        if string[i] == "(":
            closed += 1

        if string[i] != "(" and string[i] != ")" and closed == 0:
            word += string[i]

        if string[i] == "(" and closed != 0:
            newObj[Key] = word
            word = ""

        if string[i] == ")":


def reverseString(string):
    word = ""
    for letter in reversed(string):
        word += letter

    return word


# A = "(bar)"
A = "(bar)Fat(rag)"
reverseInParentheses(A)
