/// <reference path="../endpoint/jornadas.js" />

var modeloCalendario = function () {
    var self = this;

    self.calendario = ko.observable();
    self.jornadas = ko.observableArray();

    /// FUNCIONES

    self.ObtenerJornadas = function () {
        $("#loading").show();
        get_jornadas(self.calendario(), self.ObtenerJornadasCallback);
    }

    self.ObtenerJornadasCallback = function (jornadas) {
        self.jornadas(jornadas);
        
        $("#loading").hide();
    }

}