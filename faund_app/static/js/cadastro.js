document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cadastro-form');

    form.addEventListener('submit', (event) => {
        // Validação simples antes do envio
        const formData = new FormData(form);
        if (!validateForm(formData)) {
            alert('Por favor, preencha todos os campos corretamente.');
            event.preventDefault();  // Cancela o envio apenas se a validação falhar
        }
    });

    function validateForm(formData) {
        // Valida se todos os campos estão preenchidos
        for (const [key, value] of formData.entries()) {
            if (!value.trim()) {
                return false;
            }
        }
        return true;
    }
});