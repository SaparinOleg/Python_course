for (let i = 1; i <= 10; i++){
    if (!(i % 3)){
        console.log(`${i} - FizBuz`)
    }
    else if (i % 2){
        console.log(`${i} - Buz`)
    }
    else if (!(i % 2)){
        console.log(`${i} - Fiz`)
    }
}
