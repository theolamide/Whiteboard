const addMin = (arr) => {
    toSum = []
    const add = arr1 => arr1.reduce((a, b) => a + b, 0);

    for (i = 0; i < arr.length; i++) {
        toSum.push(Math.min(...arr[i]))
    }
    console.log("to sum =", toSum)
    console.log("Sum of all minimums", add(toSum));
}

addMin([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])