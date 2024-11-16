document.addEventListener("DOMContentLoaded", function(){
    const ongCheckbox = document.getElementById("ONG");
    const tutorCheckbox = document.getElementById("tutor");
    const form = document.getElementById("check");

    ongCheckbox.addEventListener("change", function(){
        if(this.checked){
            tutorCheckbox.checked = false;
        }
    });
    tutorCheckbox.addEventListener("change", function(){
        if(this.checked){
            ongCheckbox.checked = false;
        }
    });
    form.addEventListener("submit", function(event){
        event.preventDefault();
        if(ongCheckbox.checked){
            window.location.href = "cadastro_ong";
        }
        if(tutorCheckbox.checked){
            window.location.href = "cadastro_tutor";
        }
        else{
            alert("Escolha uma opção!");
        }
    });
});

function redirectUser() {
    var ongChecked = document.getElementById('ONG').checked;
    var tutorChecked = document.getElementById('tutor').checked;

    if (ongChecked && tutorChecked) {
        alert('Selecione apenas uma opção!');
    } else if (ongChecked) {
        window.location.href = 'cadastro_ong'; 
    } else if (tutorChecked) {
        window.location.href = 'cadastro_tutor'; 
    } else {
        alert('Selecione uma opção!');
    }
}
