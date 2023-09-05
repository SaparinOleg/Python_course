// https://www.codewars.com/kata/554b4ac871d6813a03000035

let numbs1 = "1 2 3 4 5" // return "5 1"
let numbs2 = "1 2 -3 4 5" // return "5 -3"
let numbs3 = "1 9 3 4 -5" // return "9 -5"

function highAndLow(numbers){
  return `${Math.max.apply(null, numbers.split(' '))} ${Math.min.apply(null, numbers.split(' '))}`
}

console.log(highAndLow(numbs1))
console.log(highAndLow(numbs2))
console.log(highAndLow(numbs3))
