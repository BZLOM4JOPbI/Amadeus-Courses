const accountButtons = document.querySelector('.accountBtnWrap').cloneNode(1);
const navButtons = document.querySelector('.navBtnWrap').cloneNode(1);
const hambButton = document.querySelector('.hambBtn');
const hamburgerMenu = document.querySelector('#hamburgerMenu');
const themeChangeBtn = document.querySelector('#changeColorTheme');


const themeDark = document.getElementById('cssDarkTheme');
themeChangeBtn.addEventListener('click', (event) => {
    if (localStorage.getItem('nightTheme')) {
        localStorage.removeItem('nightTheme');
        themeDark.setAttribute('href', '');
        return
    }
    themeDark.setAttribute('href', '/static/main_pages/css/dark_style.css');
    localStorage.setItem('nightTheme', true);
});

if (localStorage.getItem('nightTheme')) {
    themeDark.setAttribute('href', '/static/main_pages/css/dark_style.css');
}

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
    document.querySelectorAll('#changeColorTheme')[1].addEventListener('click', (event) => {
        themeDark.setAttribute('href', 'static/main_pages/css/dark_style.css')
    })
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
// Проверка на расширение дисплея с активным бургером