function myBubbleSort(arr, comparisonOperator = (a, b) => `${a}` > `${b}`) {
    let flag, end = arr.length - 1
    do {
        flag = true
        for (let i = 0; i < end; i++) {
            if (comparisonOperator(arr[i], arr[i + 1]) > 0) {
                let temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                flag = false
            }
        }
        end--
    }
    while (flag === false)
    return arr
}

function mySelectSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let minIndex = i;
        for (let index = i + 1; index < arr.length; index++) {
            if (arr[index] < arr[minIndex])
                minIndex = index;
        }
        let tmp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = tmp;
    }
    return arr;
}


console.log(mySelectSort([1, 100, 5, 9, 3, 8, 2, 0, 7, 4, 6]))

console.log(myBubbleSort(['g', 'c', 'b', 'd', 'b', 'a', 'f', 'e']))
console.log(myBubbleSort([1, 100, 5, 9, 3, 8, 2, 0, 7, 4, 6]))
console.log(myBubbleSort([1, 100, 5, 9, 3, 8, 2, 0, 7, 4, 6], (a, b) => a > b))
console.log(myBubbleSort([3, 2, 1, 30, 20, 10, 300, 200, 100], (a, b) => a < b))
