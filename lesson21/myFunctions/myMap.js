function myMap(arr, func = arr => arr) {
    let result = []
    for (let i = 0; i < arr.length; i++) {
        result.push(func(arr[i], i, arr))
    }
    return result
}


let a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(myMap(a, (x, y) => x + y * 2))
