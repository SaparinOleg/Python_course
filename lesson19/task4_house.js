const roomsOnFloor = 3
const floors = 9
const roomNumber = 666

function floor_porch(roomNumber){
    let roomsInPorch = floors * roomsOnFloor
    let porch = 1, floor = 1
    for (; roomNumber > roomsInPorch; roomNumber -= roomsInPorch, porch++) {} //Знаю, что это while, но очень хочется
    for (; roomNumber > roomsOnFloor; roomNumber -= roomsOnFloor, floor++) {}
    return `porch №${porch}, floor №${floor}`
}
console.log(floor_porch(roomNumber))
