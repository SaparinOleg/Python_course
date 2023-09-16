function mySome(arr, func = arr => arr) {
    for (let i of arr) {
        if (func(i)) {
            return true
        }
    }
    return false
}


let a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(mySome(a, elem => elem % 2 == 1))
console.log(mySome(a, elem => elem % 4 == 0))
console.log(mySome(a, elem => elem - 5 == 5))
console.log(mySome(a, elem => elem < 15))
console.log(mySome(a, elem => elem > 15))
