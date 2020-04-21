// Given an object / dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
// For example, given the following object / dictionary as input:
A = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}

const addIntegers = (obj) => {

    numArr = []
    const add = arr1 => arr1.reduce((a, b) => a + b, 0);
    for (key in obj) {
        if (typeof obj[key] == "number") {
            numArr.push(obj[key])
        }
    }

    console.log(add(numArr))
}

addIntegers(A)