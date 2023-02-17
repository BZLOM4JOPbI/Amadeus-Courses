const cardsArr = document.querySelectorAll('.card');
const decreaseSize = (event) => {
    event.target.style.animation = 'decreaseScale .3s';
}
for (let card of cardsArr) {
    card.addEventListener('mouseleave', decreaseSize);
    card.addEventListener('mouseenter', (event) => {
        event.target.style.animation = '';
    }, true );
}