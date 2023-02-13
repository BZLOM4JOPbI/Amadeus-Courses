const cards = document.querySelectorAll('.card');


const decreaseSize = (event) => {
    event.target.style.animation = 'decreaseScale .3s';
    console.log('mouseleave');
}


for (let card of cards) {
    card.addEventListener('mouseleave', decreaseSize);
    card.addEventListener('mouseenter', (event) => {
        event.target.style.animation = '';
    }, true );
}


function num(arrayOfSheep) {
    const newWords = arrayOfSheep.filter(function (word) {
        word.startsWith('a');
    })
    console.log(newWords)
}
num(['абсанс', 'вареца', 'льгозанисия', 'анубисасо', 'фия',])