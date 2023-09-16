function myReverse(arr) {
    let result = []
    for (let i = arr.length - 1; i >= 0; i--) {
        result.push(arr[i])
    }
    return result
}

console.log(myReverse([1, 2, 3, 4, 5, 6, 7, 8]))
