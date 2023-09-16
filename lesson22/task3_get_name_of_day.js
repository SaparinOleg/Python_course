const namesOfDays = {
    ua: ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П`ятниця', 'Субота', 'Неділя'],
    en: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
}


function getNameOfDay(lang, day) {
    return namesOfDays[lang][day - 1]
}


console.log(getNameOfDay('ua', 5))
console.log(getNameOfDay('en', 7))
