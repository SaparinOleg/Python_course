const sheetsInReamPaper = 500
const consumptionPerWeek = 1200
const weeksAmount = 8

let totalAmountOfSheets = consumptionPerWeek * weeksAmount
let result = 0
for (; totalAmountOfSheets > 0; totalAmountOfSheets -= sheetsInReamPaper, result++){}

console.log(result)
