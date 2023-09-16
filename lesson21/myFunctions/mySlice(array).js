function mySlice(arr, start = 0, end = arr.length) {
    let result = []
    let resultIndex = 0
    end = end < 0 ? end + arr.length : end
    start = start < 0 ? start + arr.length : start
    for (let i = start; i < end; i++) {
        result[resultIndex] = arr[i]
        resultIndex++
    }
    return result
}


let a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(mySlice(a))
console.log(mySlice(a, 7))
console.log(mySlice(a, 2, 6))
console.log(mySlice(a, 5, -4))
console.log(mySlice(a, 3, -10))
console.log(mySlice(a, -10, 2))
console.log(mySlice(a, -5, -3))
console.log(mySlice(a, -2))
