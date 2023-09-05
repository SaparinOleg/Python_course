// https://www.codewars.com/kata/57a37f3cbb99449513000cd8

function getNumberFromString(s) {
    return +(s.match(/\d/g)).join('')
  }

  console.log(getNumberFromString('fj49n3 43 4!!3 n 63, 3 4j39f'))
