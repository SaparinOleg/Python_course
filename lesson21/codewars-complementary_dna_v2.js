// https://www.codewars.com/kata/554e4a2f232cdd87d9000038

let dna1 = "AAAA" // "TTTT"
let dna2 = "ATTAGC" // "TAATCG"
let dna3 = "GTAT" // "CATA"

function DNAStrand(dna){
  return dna.replace(/./g, i => ({'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[i]))
}

console.log(DNAStrand(dna1))
console.log(DNAStrand(dna2))
console.log(DNAStrand(dna3))
