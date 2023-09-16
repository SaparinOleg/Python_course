function sumOfLowest(arr) {
    arr.sort((a, b) => a > b)
    return arr[0] + arr[1]
}

console.log(sumOfLowest([10, 800, 3453000, 8010]))
console.log(sumOfLowest([12, 898, 899, 900]))
console.log(sumOfLowest([19, 5, 42, 2, 77]))
