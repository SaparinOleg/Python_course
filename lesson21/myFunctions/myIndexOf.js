function myIndexOf(str, substr) {
    for (let i = 0; i < str.length; i++) {
        if (str[i] == substr[0] && str.slice(i, i + substr.length) == substr) {
            return i
        }
    }
    return -1
}


console.log(myIndexOf('abcdifghijklmnopqrstuvwxyz', 'l'))
console.log(myIndexOf('abcdifghijklmnopqrstuvwxyz', 'mnop'))
console.log(myIndexOf('abcdifghijklmnopqrstuvwxyz', 'foo'))
