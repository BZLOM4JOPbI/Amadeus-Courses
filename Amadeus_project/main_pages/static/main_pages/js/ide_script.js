const ide = ace.edit('editor');
// IDE Options
let ideDefaultValue = '// Put your code here';
ide.setValue(ideDefaultValue);
ide.setTheme('ace/theme/clouds');
ide.session.setMode('ace/mode/javascript');
ide.setOptions({
    fontSize: '18px',
    enableBasicAutocompletion: true,
    enableLiveAutocompletion: true,
});

// Main funcional buttons
let outputToConsoleBtn = document.querySelector('.resultBtn');
let resetBtn = document.querySelector('.resetBtn');


const getCodeResult = () => {
    let input = ide.getValue();
    let str = 'const originalLog = console.log;console.log = function (...value) {originalLog.apply(console, value);return value;};'
    // input = 'out = "";console.log = function(val){out = out + " " + val; return out;};' + input;
    input = str + input;
    try {
        input = eval(input);
    } catch (err) {
        input = err;
    }
    return input
};


outputToConsoleBtn.addEventListener('click', (event) => {
    addLogs(getCodeResult());
});


resetBtn.addEventListener('click', (event) => {
    ide.setValue(ideDefaultValue);
});


// Консоль
const consoleLogs = document.querySelector('.consoleLogs');
const resetConsole = document.querySelector('.console > .Btn');


const addLogs = (input) => {
    const log = document.createElement('li');
    log.textContent = `>  ${input}`;
    consoleLogs.appendChild(log);
};


resetConsole.addEventListener('click', (event) => {
    consoleLogs.innerHTML = '';
})


// Проверка Решения
const completeBtn = document.querySelector('.completeBtn');
const ideContainer = document.querySelector('.editorContainer');
const ideBtnsGoup = document.querySelector('.ideBtnWrap');
const tastCompleteResult = document.createElement('div')
tastCompleteResult.className = 'notification';
const rightTestValue = {
    'task1.html' : 'Hello, World!',
};

const completeTask = () => {
    const keyOfTestValue = location.href.split('/')[3];
    if (getCodeResult() == rightTestValue[keyOfTestValue]) {
        addLogs(getCodeResult());
        completeBtn.textContent = 'Решить еще раз'
        tastCompleteResult.style.backgroundColor = 'rgba(89, 138, 118, 0.6)'
        tastCompleteResult.textContent = 'Задание выполнено'
        ideContainer.insertBefore(tastCompleteResult, ideBtnsGoup);
    } else {
        addLogs(getCodeResult());
        tastCompleteResult.style.backgroundColor = 'rgba(164, 50, 64, 0.5)'
        tastCompleteResult.textContent = 'Попробуйте еще раз'
        ideContainer.insertBefore(tastCompleteResult, ideBtnsGoup);
    }

}   
completeBtn.addEventListener('click', completeTask);