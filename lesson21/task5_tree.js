let medianNumber = 15
let sharps = 1

while (medianNumber > 0){
    console.log('-'.repeat(medianNumber - 1) + '#'.repeat(sharps) + '-'.repeat(medianNumber - 1))
    medianNumber--
    sharps += 2
}
