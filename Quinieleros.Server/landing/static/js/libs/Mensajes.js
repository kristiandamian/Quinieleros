
$(document).ready(function () {
    //Objeto añadido a Jquery que nos permite acceder a las utilerias
    $.utils = {};

    //Regresa a nulo todos los observables de un objeto
    $.utils.limpiarModelo = function (obj) {
        for (var prop in obj) {

            if (obj.hasOwnProperty(prop)
                    && ko.isObservable(obj[prop])
                    && !ko.isComputed(obj[prop])
                    && obj[prop]() != null
                    && !(obj[prop]().push) //Para revisar si no es un array
                ) {
                obj[prop](undefined);

            }
        }

        //if (listas) {
        //    for (var i = 0; i < listas.length; i++) {
        //        jq142("#" + listas[i]).ufd('destroy');
        //        jq142("#" + listas[i]).ufd({ log: true });
        //    }
        //}
    }
    //stackoverflow.com/questions/19491336/get-url-parameter-jquery
    $.utils.urlParam = function (name) {
        var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
        if (results == null) {
            return null;
        }
        else {
            return results[1] || 0;
        }
    }

    //Muestra mensaje con alerta bootstrap
    $.utils.MuestroMensaje = function (mensaje, clase, callback) {
        var div = "mensajes"
        $("#" + div).empty();
        $("#" + div).removeClass("alert-success");
        $("#" + div).removeClass("alert-info");
        $("#" + div).removeClass("alert-danger");
        $("#" + div).removeClass("alert-warning");
        $("#" + div).append('<a href="#" class="close" onclick="$(&#39;.alert&#39;).hide()" >&times;</a>');
        $("#" + div).append(mensaje);
        $("#" + div).addClass(clase);
        $("#" + div).show();
        $('html, body').animate({
            scrollTop: -20,
            scrollLeft: -20
        });
        if (callback)
            callback();
    }

    $.utils.OcultoMensaje = function () {
        $('.alert').hide()
    }
});