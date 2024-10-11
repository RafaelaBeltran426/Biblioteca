// Validar el formulario de registro de usuario
document.addEventListener("DOMContentLoaded", function () {
    const formRegistrarUsuario = document.querySelector("form[action='/registrar_usuario']");
    formRegistrarUsuario.addEventListener("submit", function (event) {
        const rut = document.querySelector("#rut").value;
        const nombre = document.querySelector("#nombre").value;

        if (!validarRUT(rut)) {
            alert("Por favor, ingrese un RUT válido.");
            event.preventDefault();  // Evitar que se envíe el formulario si el RUT no es válido
        } else if (nombre.trim() === "") {
            alert("El nombre no puede estar vacío.");
            event.preventDefault();
        }
    });

    // Función simple para validar el RUT (puedes mejorarla según tu lógica)
    function validarRUT(rut) {
        const regex = /^[0-9]+-[0-9kK]{1}$/;  // Un formato básico de RUT, por ejemplo, 12345678-9 o 12345678-K
        return regex.test(rut);
    }

    // Confirmar préstamo de libro
    const formsPrestar = document.querySelectorAll("form[action^='/prestar_libro']");
    formsPrestar.forEach(function(form) {
        form.addEventListener("submit", function(event) {
            const confirmacion = confirm("¿Estás seguro de que deseas prestar este libro?");
            if (!confirmacion) {
                event.preventDefault();
            }
        });
    });

    // Confirmar devolución de libro
    const formsDevolver = document.querySelectorAll("form[action^='/devolver_libro']");
    formsDevolver.forEach(function(form) {
        form.addEventListener("submit", function(event) {
            const confirmacion = confirm("¿Estás seguro de que deseas devolver este libro?");
            if (!confirmacion) {
                event.preventDefault();
            }
        });
    });
});
