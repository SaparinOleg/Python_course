function myReplace(str, substr, replacement) {
    let result = ''
    for (let i = 0; i < str.indexOf(substr); i++) {
        result += str[i]
    }
    result += replacement
    for (let i = str.indexOf(substr) + substr.length; i < str.length; i++) {
        result += str[i]
    }
    return result
}


console.log(myReplace('Jack is my friend. Jack is a doctor.', 'Jack', 'Paul'))
console.log(myReplace('I hate Jack. Mark is my friend.', 'Jack', 'Paul'))
console.log(myReplace('Hello. My name is Molly.', 'Molly', 'Alexandr'))
