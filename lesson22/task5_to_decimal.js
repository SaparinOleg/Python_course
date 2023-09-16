function toDecimal(arr) {
    return arr.reverse().reduce((acc, item, index) => acc + item * (2 ** index))
}

let a = [0, 0, 0, 1] // 1
let b = [0, 0, 1, 0] // 2
let c = [0, 1, 0, 1] // 5
let d = [1, 0, 0, 1] // 9
let e = [0, 1, 1, 0] // 6
let f = [1, 1, 1, 1] // 15
let g = [1, 0, 1, 1] // 11
let h = [1, 0, 0, 0, 1] // 17
let i = [1, 0, 0, 1, 0] // 18
let j = [1, 0, 1, 0, 1] // 21
let k = [1, 1, 1, 0, 0, 1] // 57

console.log(toDecimal(j))
