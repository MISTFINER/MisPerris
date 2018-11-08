/*Función Para que el Usuario deba ingresar una fecha de Nacimiento Menor al Año 2001*/
$('#fechaNac').change(function() {
    var fecha = new Date($('#fechaNac').val());
    if (fecha.getFullYear() > 2001) {
        alert("La fecha de Nacimiento Debe ser Anterior al Año 2001")
return;
}
});