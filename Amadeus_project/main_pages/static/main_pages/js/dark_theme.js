themeDark = document.getElementById('cssDarkTheme');  
if (localStorage.getItem('nightTheme')) {
    themeDark.setAttribute('href', '/static/main_pages/css/dark_style.css');
}