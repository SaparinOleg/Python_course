function myShift(array, ...params) {
    let index = params.length
    for (let elem of array) {
        params[index] = elem
        index++
    }
    return params
}

function myShift2(array, ...params) {
    return [...params, ...array]
}


console.log(myShift([1, 2, 3, 4, 5], 'a', 'b', '666'))
console.log(myShift2([1, 2, 3, 4, 5], 'a', 'b', '666'))
