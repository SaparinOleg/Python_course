function myPush(array, ...params) {
    let index = array.length
    for (let elem of params) {
        array[index] = elem
        index++
    }
    return array
}

function myPush2(array, ...params) {
    return [...array, ...params]
}


console.log(myPush([1, 2, 3, 4, 5], 'a', 'b', '666'))
console.log(myPush2([1, 2, 3, 4, 5], 'a', 'b', '666'))
