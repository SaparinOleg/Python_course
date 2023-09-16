function myLength(str) {
    let i = 0
    while (str[i] != undefined) {
        i++
    }
    return i
}


console.log(myLength('abcdifghijklmnopqrstuvwxyz'))
