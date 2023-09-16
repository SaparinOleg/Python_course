function mySubstring(str, start, end) {
    let result = ''
    for (let i = start; i < end; i++) {
        result += str[i]
    }
    return result
}


console.log(mySubstring('Here is Jonny!', 5, 7))
