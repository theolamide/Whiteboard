# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
A = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}


def addIntegers(obj):

    num = 0
    for key in obj:
        if type(obj[key]) == int:
            num += obj[key]

    print(num)


addIntegers(A)
