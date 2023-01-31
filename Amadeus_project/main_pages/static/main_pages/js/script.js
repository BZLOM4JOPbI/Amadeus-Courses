const accountButtons = document.querySelector('.accountBtnWrap').cloneNode(1);
const navButtons = document.querySelector('.navBtnWrap').cloneNode(1);
const hambButton = document.querySelector('.hambBtn');
const hamburgerMenu = document.querySelector('#hamburgerMenu');


const mediaQuery = window.matchMedia('(min-width: 751px)'); // Медиазапрос на увелечение экрана выше брейкпоинта

const hambClick = () => {
    if (Boolean(hamburgerMenu.children.length)) {
        hamburgerMenu.removeChild(navButtons);
        hamburgerMenu.removeChild(accountButtons);
        return
    }
    navButtons.style.display = 'block';
    hamburgerMenu.appendChild(navButtons);
    accountButtons.style.display = 'flex';
    hamburgerMenu.appendChild(accountButtons);
    setInterval(hamburgerAviable, 1500);
};

hambButton.addEventListener('click', hambClick);

const footerYear = document.querySelector('.footerSubtitle');
let now = new Date();
footerYear.textContent = 'Copyright ' + footerYear.textContent + now.getFullYear() + '. All rights reserved.';

const hamburgerAviable = () => {
    if (mediaQuery.matches && Boolean(hamburgerMenu.children.length)) {
        hamburgerMenu.removeChild(navButtons);
        hamburgerMenu.removeChild(accountButtons);
    }
};
// Проверка на расширение дисплеия с активным бургером