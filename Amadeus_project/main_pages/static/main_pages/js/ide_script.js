const ide = ace.edit('editor');
const taskValuesForIde = {
    '1': '// Put your code here',
    '4': 'let V = 24; // Скорость\nlet t = 2; // Время',
    '3': 'console.log(5 _ (2 _ 6) _ 2);',
    '2': '// Put your code here',
}

// IDE Options
const keyOfTestValue = location.href.split('/')[4];
let ideDefaultValue = '1234'.includes(keyOfTestValue) ? taskValuesForIde[keyOfTestValue] : '// Put your code here';
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
    console.log(getCodeResult())
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
    '2' : 'Hello, World!',
    '4' : 48,
    '3' : 38,
    '1' : 'Смузихлеб Иван - лучший фронт'
};
const messageTaskComplete = { 
    complete: 'yes',
    task: keyOfTestValue,
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const sendRequest = async (url, method, body = null) => {
    console.log('Запрос отправлен');
    const csrftoken = getCookie('csrftoken');
    return fetch(url, {
        method: method,
        body: method === 'POST' ?  JSON.stringify(body) : null,
        headers: { 'Content-Type': 'application/json;charset=utf-8', 'X-CSRFToken': csrftoken },
    }).then(response => {
        return response.json()
    })
}

const completeTask = async () => {
    messageTaskComplete.ideValue = ide.getValue();
    addLogs(getCodeResult());
    if (getCodeResult()[0] === rightTestValue[keyOfTestValue]) {
        completeBtn.textContent = 'Решить еще раз';
        tastCompleteResult.style.backgroundColor = 'rgba(89, 138, 118, 0.6)';
        tastCompleteResult.textContent = 'Задание выполнено';
        sendRequest('/Amadeus_project/main_pages/views', 'POST', messageTaskComplete).then(data => console.log(data))
    } else if (keyOfTestValue == '1') {
        tastCompleteResult.style.backgroundColor = 'rgba(89, 138, 118, 0.6)';
        tastCompleteResult.textContent = 'Задание выполнено';
        sendRequest('/Amadeus_project/main_pages/views', 'POST', messageTaskComplete).then(data => console.log(data))
    } else {
        tastCompleteResult.style.backgroundColor = 'rgba(164, 50, 64, 0.5)';
        tastCompleteResult.textContent = 'Попробуйте еще раз';
    }
    ideContainer.insertBefore(tastCompleteResult, ideBtnsGoup);
    return
}   
try {
    completeBtn.addEventListener('click', completeTask);
} catch (err) {
    //pass
}   
const sendRequestBtn = document.querySelector('.BtnGetRequest');
// const button = document.getElementById('Btn');
sendRequestBtn.addEventListener('click', () => sendRequest('https://jsonplaceholder.typicode.com/users', 'GET', ).then(data => console.log(data)), true)
