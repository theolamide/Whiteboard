A = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}


def addIntegers(obj):

    numArr = []
    for key in obj:
        if type(obj[key]) == int:
            numArr.append(obj[key])

    print(sum(numArr))


addIntegers(A)
