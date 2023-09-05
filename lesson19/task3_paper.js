const sheetsInReamPaper = 500
const consumptionPerWeek = 1200
const weeksAmount = 8
let totalConsumption = consumptionPerWeek * weeksAmount
console.log((totalConsumption - totalConsumption % sheetsInReamPaper) / sheetsInReamPaper)
