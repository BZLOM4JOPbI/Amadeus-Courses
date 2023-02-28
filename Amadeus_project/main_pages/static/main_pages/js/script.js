// Hamburger Menu

const accountButtons = document.querySelector('.accountBtnWrap').cloneNode(1);
accountButtons.classList.add('inHam');
const navButtons = document.querySelector('.navBtnWrap').cloneNode(1);
navButtons.classList.add('inHam');
const hambButton = document.querySelector('.hambBtn');
const hamburgerMenu = document.querySelector('#hamburgerMenu');


const hambClick = () => {
    if (Boolean(hamburgerMenu.children.length)) {
        hamburgerMenu.removeChild(navButtons);
        hamburgerMenu.removeChild(accountButtons);
        return
    }
    hamburgerMenu.appendChild(navButtons);
    hamburgerMenu.appendChild(accountButtons);
    document.querySelectorAll('#changeColorTheme')[1].addEventListener('click', changeThemeFun);
    if (localStorage.getItem('nightTheme')) {
        document.querySelectorAll('#changeColorTheme')[1].checked = 'True';
    }
};

hambButton.addEventListener('click', hambClick);

// Hamburger End



// Dark Theme
const themeChangeBtn = document.querySelector('#changeColorTheme');
const themeDark = document.getElementById('cssDarkTheme');


const changeThemeFun = (event) => {
    if (localStorage.getItem('nightTheme')) {
        localStorage.removeItem('nightTheme');
        themeDark.setAttribute('href', '/static/main_pages/css/light_style.css');
        try {
            ide.setTheme('ace/theme/clouds');
        } catch {
            //pass
        }
        return
    }
    themeDark.setAttribute('href', '/static/main_pages/css/dark_style.css');
    localStorage.setItem('nightTheme', true);
    try {
        ide.setTheme('ace/theme/tomorrow_night');
    } catch {
        //pass
    }
}

themeChangeBtn.addEventListener('click', changeThemeFun);

if (localStorage.getItem('nightTheme')) {
    themeChangeBtn.checked = 'True';
    themeDark.setAttribute('href', '/static/main_pages/css/dark_style.css');
    try {
        ide.setTheme('ace/theme/tomorrow_night');
    } catch {
        //pass
    }
}   
// Dark Theme End

// Footer Year

const footerYear = document.querySelector('.footerSubtitle');
let now = new Date();
footerYear.textContent = 'Copyright ' + footerYear.textContent + now.getFullYear() + '. All rights reserved.';

// Footer Year End

// ANimation 
// const textAreas = document.querySelectorAll('p input');
// const animation = document.querySelector('.loadAnim');
// const submitBtn = document.querySelector('input[type="submit"]');
// submitBtn.addEventListener('click', () =>{
//     console.log(textAreas.values());
//     animation.style.display = 'flex';
// })