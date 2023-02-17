const formPassWrap = document.querySelectorAll('p:has(input[type="password"]');
const createEyeOnPass = () => {
    const eyeOnPass = document.createElement('img');
    eyeOnPass.setAttribute('src', 'Amadeus_project/main_pages/static/main_pages/img/eye-regular.svg')
    return eyeOnPass
};
for (pass of formPassWrap) {
    pass.addChild(createEyeOnPass);
}