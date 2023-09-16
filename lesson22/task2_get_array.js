function getArray(amount=3) {
  let result = []
  for (let i = 1; i < amount; i += 3) {
    result.push([i, i + 1, i + 2])
  }
  return result
}


console.log(getArray(15))
