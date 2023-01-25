//var editor = document.querySelector('#editor');\
const ide = ace.edit('editor');

/*ace.edit(editor, {
    theme: 'ace/theme/eclipse',
    mode: 'ace/mode/javascript',
    fontSize: 18,
});*/
ide.setOptions({
    fontSize: '18px',
    mode: 'ace/mode/javascript',
    theme: 'ace/theme/eclipse',
})
let result = document.querySelector('.resultBtn');
const getResult = () => {
    result.textContent = ide.getValue();
};
result.addEventListener('click', getResult);
