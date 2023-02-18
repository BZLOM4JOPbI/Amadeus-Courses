// Ответы на задачи
const rightTestValue = {
    '2' : 'Hello, World!',
    '4' : 48,
    '3' : 38,
    '1' : 'Смузихлеб Иван - лучший фронт'
};
//
// Файл на бэк
const messageTaskComplete = { 
    complete: 'yes',
    task: keyOfTestValue,
}
//
// Элементы для task`ов
const completeBtn = document.querySelector('.completeBtn');
const ideContainer = document.querySelector('.editorContainer');
const ideBtnsGoup = document.querySelector('.ideBtnWrap');
//
// Результат решения
const tastCompleteResult = document.createElement('div')
tastCompleteResult.className = 'notification';
//
// Вытягиваем токен из кукей
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
//
// Функция для запросов запрос
const sendRequest = async (url, method, body = null) => {
    const csrftoken = getCookie('csrftoken');
    return fetch(url, {
        method: method,
        body: method === 'POST' ?  JSON.stringify(body) : null,
        headers: { 'Content-Type': 'application/json;charset=utf-8', 'X-CSRFToken': csrftoken },
    }).then(response => {
        return response.json()
    })
}
//
// Завершение task`а
const completeTask = async () => {
    messageTaskComplete.ideValue = ide.getValue();
    addLogs(getCodeResult());
    if (getCodeResult()[0] === rightTestValue[keyOfTestValue] || keyOfTestValue == '1') {
        completeBtn.textContent = 'Решить еще раз';
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
completeBtn.addEventListener('click', completeTask);
//
// sendRequest('/Amadeus_project/main_pages/views', 'GET', )
//     .then(data => ide.setValue(data.code))
//     .catch(err => console.log(err))
//