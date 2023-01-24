var editor = document.querySelector('#editor');

ace.edit(editor, {
    theme: 'ace/theme/eclipse',
    mode: 'ace/mode/javascript',
    fontSize: 18,
});
//pass