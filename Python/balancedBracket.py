def balancedBrackets(string):
    # Write your code here
    print(string)
    toCheck = []
    singlePole = 0

    if "[" or "]" or "(" or ")" or "{" or "}" or "|" in string:
        for i in range(0, len(string)):
            print(string[i])
            print(toCheck)
            if string[i].isalnum() is False and string[i] == "[":
                toCheck.append(string[i])
            elif string[i].isalnum() is False and string[i] == "(":
                toCheck.append(string[i])
            elif string[i].isalnum() is False and string[i] == "{":
                toCheck.append(string[i])
            elif string[i].isalnum() is False and string[i] == "|":
                if singlePole == 0:
                    toCheck.append(string[i])
                    singlePole += 1
                elif toCheck[-1] == "|" and singlePole == 1:
                    toCheck.pop(-1)
                else:
                    toCheck.append(string[i])
            elif string[i].isalnum() is False and string[i] == "]":
                if toCheck[-1] == "[":
                    toCheck.pop(-1)
                else:
                    print("False")
                    return False
            elif string[i].isalnum() is False and string[i] == ")":
                if toCheck[-1] == "(":
                    toCheck.pop(-1)
                else:
                    print("False")
                    return False
            elif string[i].isalnum() is False and string[i] == "}":
                if toCheck[-1] == "{":
                    toCheck.pop(-1)
                else:
                    print("False")
                    return False

        if len(toCheck) < 1:
            print("True")
            return True
        else:
            print("False")
            return False

    return False


String = "He ran| |out of money, so he {| had} to stop playing | poker."
balancedBrackets(String)
