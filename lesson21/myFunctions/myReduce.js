function myReduce(arr, reducer = acc => acc, acc = 0) {
    for (let i = 0; i < arr.length; i++) {
        acc = reducer(acc, arr[i], i, arr)
    }
    return acc
}

let a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(myReduce(a, (x, y) => x + y))

let b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
console.log(myReduce(b, (acc, item, index) => {
    acc.push(`Под индексом №${index}, находится ${item}\n`)
    return acc
}, []))

let fruitBasket = ['banana', 'cherry', 'orange', 'apple', 'cherry', 'orange', 'apple', 'banana', 'cherry', 'orange', 'fig']
console.log(myReduce(fruitBasket, (counter, fruit) => {
    counter[fruit] = (counter[fruit] || 0) + 1
    return counter
}, {}))
