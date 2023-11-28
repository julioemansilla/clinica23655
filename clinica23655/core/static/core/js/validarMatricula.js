let matricula = document.getElementById("matricula");
    
matricula.addEventListener("input", validarMatricula)
function validarMatricula(e){     
    let leyenda = document.getElementById("leyenda");
    if (e.target.value.length < 6) {
        matricula.classList.remove('is-valid');
        matricula.classList.add('is-invalid');
        if(!leyenda){
            leyenda = document.createElement('p');
            leyenda.id = 'leyenda';
            leyenda.textContent = 'Debe contener más de 6 caracteres.';
            matricula.parentNode.appendChild(leyenda);
        }
    } else {
        matricula.classList.remove('is-invalid');
        matricula.classList.add('is-valid');
        if (leyenda) {
            leyenda.parentNode.removeChild(leyenda);
       }
    }
}