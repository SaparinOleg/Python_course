// https://www.codewars.com/kata/554e4a2f232cdd87d9000038

let dna1 = "AAAA" // "TTTT"
let dna2 = "ATTAGC" // "TAATCG"
let dna3 = "GTAT" // "CATA"

function DNAStrand(dna){
  let result = []
  for (let item of dna){
    switch (item){
      case 'A':
        result.push('T')
        break
      case 'T':
        result.push('A')
        break
      case 'G':
        result.push('C')
        break
      case 'C':
        result.push('G')
    }
  }
  return result.join('')
}

console.log(DNAStrand(dna1))
console.log(DNAStrand(dna2))
console.log(DNAStrand(dna3))
