function myRepeat(str, num) {
    if (num < 0) {
        return 'RangeError'
    }
    else if (num == 0) {
        return ''
    }
    let resultString = ''
    for (; num > 0; resultString += str, num--) { }
    return resultString
}


console.log(myRepeat('abc|', 10))
