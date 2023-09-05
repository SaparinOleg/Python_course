// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

let str = "zpglnRxqenU" // "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"

function accum(s){
  let result = [s[0].toUpperCase()]
  for (let i = 1; i < s.length; i++){
    result += `-${s[i].toUpperCase()}${s[i].repeat(i).toLowerCase()}`
  }
  return result
}

console.log(accum(str))
