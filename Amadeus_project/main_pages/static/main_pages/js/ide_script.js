const ide = ace.edit('editor');

ide.setTheme('ace/theme/clouds');
ide.session.setMode('ace/mode/javascript');
ide.setOptions({
    fontSize: '18px',
    enableBasicAutocompletion: true,
    enableLiveAutocompletion: true,
});
const getCode = () => {
    return ide.getValue()
};
let outputBtn = document.querySelector('.resultBtn') 
outputBtn.addEventListener('click', (event) => {
    let valueIde = getCode();
    try {
        console.log(new Function(valueIde)())
    } catch (err) {
        console.error(err)
    }

});