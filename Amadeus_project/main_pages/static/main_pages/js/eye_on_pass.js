const formPassWrap = document.querySelectorAll('p:has(input[type="password"]');
for (pass of formPassWrap) {
    pass.classList.add('eyeOpen')
    pass.addEventListener('click', (event) => {
        event.target.classList.toggle('eyeOpen');
        event.target.classList.toggle('eyeClose');
        if (event.target.classList[0] == 'eyeOpen') {
            event.target.childNodes[3].type = 'password';
            return
        }
        event.target.childNodes[3].type = 'text';
    })
}