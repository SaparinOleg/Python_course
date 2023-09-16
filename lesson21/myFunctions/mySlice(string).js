function mySlice(str, start = 0, end = str.length) {
    let result = ''
    end = end < 0 ? str.length + end : end
    start = start < 0 ? str.length + start : start
    for (let i = start; i < end; i++) {
        result += str[i]
    }
    return result
}


let a = '0123456789'
console.log(mySlice(a))
console.log(mySlice(a, 7))
console.log(mySlice(a, 2, 6))
console.log(mySlice(a, 5, -4))
console.log(mySlice(a, 3, -10))
console.log(mySlice(a, -10, 2))
console.log(mySlice(a, -5, -3))
console.log(mySlice(a, -2))
