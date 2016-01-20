/// <reference path="../endpoint/grupos.js" />

var modeloProfile = function () {
    var self = this;
    self.usuario = ko.observable();
    self.nombre = ko.observable();
    self.grupos = ko.observableArray();

    ///// FUNCIONES BABY
    self.ObtenerGrupos = function (usuario, nombre) {
        $("#loading").show();
        self.usuario(usuario);
        self.nombre(nombre);
        get_grupo_byUser(self.usuario(), self.ObtenerGruposCallback);
    }

    self.ObtenerGruposCallback = function (grupos) {
        self.grupos(grupos);
        $("#loading").hide();
    }

    self.addGrupo = function () {

    }
}