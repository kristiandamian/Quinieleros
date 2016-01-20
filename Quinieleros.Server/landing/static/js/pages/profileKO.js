/// <reference path="../endpoint/grupos.js" />
/// <reference path="../endpoint/ligas.js" />
/// <reference path="../endpoint/calendarios.js" />

var modeloProfile = function () {
    var self = this;
    self.usuario = ko.observable();
    self.nombre = ko.observable();
    self.grupos = ko.observableArray();
    self.liga = ko.observable();
    self.ligas = ko.observableArray();
    self.calendario = ko.observable();
    self.calendarios = ko.observableArray();
    self.MostrarNoGrupos = ko.observable(false);

    ///// FUNCIONES BABY
    self.ObtenerGrupos = function (usuario, nombre) {
        $("#loading").show();
        self.usuario(usuario);
        self.nombre(nombre);
        get_grupo_byUser(self.usuario(), self.ObtenerGruposCallback);
    }

    self.ObtenerGruposCallback = function (grupos) {
        self.grupos(grupos);
        console.log(self.grupos().length <= 0);
        var mostrar = self.grupos().length <= 0;
        self.MostrarNoGrupos(mostrar);
        $("#loading").hide();
    }

    self.ObtenerLigas = function () {
        $("#loading").show();
        get_ligas(self.ObtenerLigasCallback);
    }

    self.ObtenerLigasCallback = function (ligas) {
        self.ligas(ligas);
        $("#loading").hide();
    }

    self.ObtenerCalendarios = function () {
        $("#loading").show();
        get_calendarios(self.liga().key, self.ObtenerCalendariosCallback);
    }

    self.ObtenerCalendariosCallback = function (calendarios) {
        self.calendarios(calendarios);
        $("#loading").hide();
    }
    self.addGrupo = function () {

    }
}