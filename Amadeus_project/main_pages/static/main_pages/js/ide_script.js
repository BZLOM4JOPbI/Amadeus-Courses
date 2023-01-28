const ide = ace.edit('editor');
// IDE Options
ide.setTheme('ace/theme/clouds');
ide.session.setMode('ace/mode/javascript');
ide.setOptions({
    fontSize: '18px',
    enableBasicAutocompletion: true,
    enableLiveAutocompletion: true,
});

// Main funcional buttons
const getCode = () => {
    return ide.getValue()
};
let outputBtn = document.querySelector('.resultBtn');
let resetBtn = document.querySelector('.resetBtn');
outputBtn.addEventListener('click', (event) => {
    let output = new Function(getCode())();
    (output) ? console.log(output) : true
});
resetBtn.addEventListener('click', (event) => {
    ide.setValue('');
});

