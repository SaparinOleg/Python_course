// https://www.codewars.com/kata/5266876b8f4bf2da9b000362

let m0 = [] //'no one likes this'
let m1 = ['Peter'] // 'Peter likes this'
let m2 = ['Jacob', 'Alex'] // 'Jacob and Alex like this'
let m3 = ['Max', 'John', 'Mark'] // 'Max, John and Mark like this'
let m4 = ['Alex', 'Jacob', 'Mark', 'Max'] // 'Alex, Jacob and 2 others like this'
let m5 = ['Stan', 'Alex', 'Jacob', 'Mark', 'Max', 'Bob'] // 'Stan, Alex and 4 others like this'

function likes(names){
  if (names.length == 0){
    return 'no one likes this'
  }
  else if (names.length == 1){
    return `${names[0]} likes this`
  }
  else if (names.length == 2){
    return `${names[0]} and ${names[1]} like this`
  }
  else if (names.length == 3){
    return `${names[0]}, ${names[1]} and ${names[2]} like this`
  }
  else{
    return `${names[0]}, ${names[1]} and ${names.length - 2} others like this`
  }
}

console.log(likes(m5))
