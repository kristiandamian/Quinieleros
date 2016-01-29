
function DatosCompletos(clase) {
    
    if (clase=="" || clase==null || clase==undefined) {
        clase="obligatorio";
    }
    var completos=true;
    $("."+clase).each(function(){
        if($(this).val()==null || $(this).val().length<=0){
            completos=false;
            $(this).addClass("alert-danger")
        }
    });
    if (!completos) 
        $.utils.MuestroMensaje("Debe capturar todos los datos obligatorios", "alert-danger");
    return completos;
}
function FormatoMoneda(cellClass) {
    $("." + cellClass).each(function () {
        var decimales = "0";
        var monto = "";
        var formateado = "";
        var re = new RegExp(',', 'g');
        $(this).text($(this).text().replace("$", "").replace(re,''));
        

        if ($(this).text().split(".").length > 1) {
            decimales = $(this).text().split(".")[1];
            if (decimales.length > 2) {
                decimales = decimales.substring(0, 2);
            }
        }
        monto = $(this).text().split(".")[0];
        var posiciones = 0;
        for (var x = monto.length - 1; x >= 0; x--) {
            if (posiciones >= 3) {
                formateado = "," + formateado;
                posiciones = 0
            }
            formateado = monto.charAt(x) + formateado;
            posiciones++;
        }
        $(this).text("$ "+formateado + "." + decimales);
    });
}
