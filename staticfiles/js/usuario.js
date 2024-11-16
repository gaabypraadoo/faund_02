function redirectUser() {
    const isOng = document.getElementById('ONG').checked;
    const isTutor = document.getElementById('tutor').checked;

    if (isOng) {
        window.location.href = urlCadastroOng;
    } else if (isTutor) {
        window.location.href = urlCadastroTutor;
    } else {
        alert('Selecione uma opção!');
    }
}