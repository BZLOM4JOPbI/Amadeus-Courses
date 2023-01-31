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
    let input = getCode();
    addLogs(input);
});
resetBtn.addEventListener('click', (event) => {
    ide.setValue('');
});
// Консоль
const consoleLogs = document.querySelector('.consoleLogs');
const addLogs = (input) => {
    const log = document.createElement('li');
    // input = 'console.oldLog = console.log;console.log = function(value){console.oldLog(value);return value;};' + input;
    input = 'out = ""; console.log = function(val){out = out + " " + val; return out;};' + input
    try {
        input = eval(input);
    } catch (err) {
        input = err;
    }
    log.textContent = `>  ${input}`;
    consoleLogs.appendChild(log);
};