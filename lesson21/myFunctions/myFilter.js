function myFilter(arr, func = arr => arr) {
    let result = []
    for (let i = 0; i < arr.length; i++) {
        if (func(arr[i], i, arr)) {
            result.push(arr[i])
        }
    }
    return result
}


let a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(myFilter(a, (x, y, a) => x % 2 == 1))
console.log(myFilter(a, (x, y, a) => y % 3 == 1))
