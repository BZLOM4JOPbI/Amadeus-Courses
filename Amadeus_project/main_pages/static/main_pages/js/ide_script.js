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
    input = 'out = ""; console.log = function(val){out = out + " " + val; return out;};' + input;
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
const rightTestValue = {
    'task1.html' : 'Hello, World',
};

const completeTask = () => {
    const keyOfTestValue = location.href.split('/')[3];
    console.log('a');
    if (getCodeResult() === rightTestValue[keyOfTestValue]) {
        console.log('Верно');
        addLogs(getCodeResult());
    }
    else {
        console.log('Ошибка');
    }
}

completeBtn.addEventListener('click', completeTask);