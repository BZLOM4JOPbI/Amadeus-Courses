// Настройка IDE
const ide = ace.edit('editor');
ide.setTheme('ace/theme/clouds');
ide.session.setMode('ace/mode/javascript');
ide.setOptions({
    fontSize: '18px',
    enableBasicAutocompletion: true,
    enableLiveAutocompletion: true,
});
//
// Значение IDE по умолчанию для ide и task`ов
const keyOfTestValue = location.href.split('/')[4];
const taskValuesForIde = {
    '1': '// Put your code here',
    '4': 'let V = 24; // Скорость\nlet t = 2; // Время',
    '3': 'console.log(5 _ (2 _ 6) _ 2);',
    '2': '// Put your code here',
}
let ideDefaultValue = '1234'.includes(keyOfTestValue) ? taskValuesForIde[keyOfTestValue] : '// Put your code here';
//
// Сброс IDE
ide.setValue(ideDefaultValue);
let resetBtn = document.querySelector('.resetBtn');
resetBtn.addEventListener('click', (event) => {
    ide.setValue(ideDefaultValue);
});
//
// Кнопка решения и вывода в консоль
let outputToConsoleBtn = document.querySelector('.resultBtn');
outputToConsoleBtn.addEventListener('click', (event) => {
    addLogs(getCodeResult());
});
//
// Выполнение кода
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
//
// Вывод результата в консоль
const consoleLogs = document.querySelector('.consoleLogs');
const resetConsole = document.querySelector('.console > .Btn');


const addLogs = (input) => {
    const log = document.createElement('li');
    if (!(Array.isArray(input))) {
        log.textContent = `>  ${input}`;
    } else {
        if (input.length > 1) {
            log.textContent = `>  ${input}`;
        } else {
            if (typeof input[0] == 'string') {
                    log.textContent = `>  '${input[0]}'`;
            } else if (Array.isArray(input[0])) {
                log.textContent = `>  [ ${input[0]} ]`;
            } else {
                log.textContent = `>  ${input[0]}`;
            }
        }
    }
    consoleLogs.appendChild(log);
};
//
// Сброс консоли
resetConsole.addEventListener('click', (event) => {
    consoleLogs.innerHTML = '';
})
// ваы