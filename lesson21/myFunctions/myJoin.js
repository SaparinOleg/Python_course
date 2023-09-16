function myJoin(array, separator) {
    if (!separator) {
        separator = ','
    }
    let result = `${array[0]}`
    for (let element = 1; element < array.length; element++) {
        result += `${separator}${array[element]}`
    }
    return result
}


console.log(myJoin(['a', 'b', 'c', 'd', 'e'], '^'))
