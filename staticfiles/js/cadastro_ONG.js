document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cadastro-form');

    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Coleta os dados do formulário
        const formData = new FormData(form);

        // Validação simples
        if (!validateForm(formData)) {
            alert('Por favor, preencha todos os campos corretamente.');
            return;
        }

        // Enviar dados para o servidor (Exemplo com fetch)
        fetch('/caminho/do/servidor', { // Ajuste o caminho conforme necessário
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Processa a resposta do servidor
            if (data.success) {
                alert('Cadastro realizado com sucesso!');
                form.reset(); // Limpa o formulário
            } else {
                alert('Ocorreu um erro ao realizar o cadastro.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Ocorreu um erro ao realizar o cadastro.');
        });
    });

    function validateForm(formData) {
        // Adicione validações conforme necessário
        for (const [key, value] of formData.entries()) {
            if (!value.trim()) {
                return false; // Retorna false se algum campo estiver vazio
            }
        }
        return true; // Retorna true se todos os campos estiverem preenchidos
    }
});
