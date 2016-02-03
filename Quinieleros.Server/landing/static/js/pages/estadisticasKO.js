/// <reference path="../endpoint/grupos.js" />
/// <reference path="../endpoint/resultados.js" />
var modeloEstadisticas = function () {
    var self = this;
    self.grupo = ko.observable();
    self.usuario = ko.observable();
    self.NombreGrupo = ko.observable();
    self.NombreJornada = ko.observable();
    self.JornadaActual = ko.observableArray();
    self.JornadaAcumulada = ko.observableArray();

    //// FUNCIONES BABY

    self.NombreGrupo = ko.computed(function () {
        return "Estadisticas del grupo " + self.NombreGrupo();
    });
    
    self.ObtenerGrupos = function () {
        $("#loading").show();
        get_grupo(self.grupo(), self.ObtenerGruposCallback);
    }

    self.ObtenerGruposCallback = function (grupo) {
        self.NombreGrupo(grupo.Nombre);
        $("#loading").hide();
    }

    self.getResultados() = function () {
        self.ObtenerResultadoJornada();
        self.ObtenerResultadoGrupo();
    }
    self.ObtenerResultadoJornada = function () {
        $("#loading").show();
        obtener_resultados_jornada_grupo(self.grupo(), self.ObtenerResultadoJornadaCallback);
    }

    self.ObtenerResultadoJornadaCallback = function (resultados) {
        self.CreoObjetoResultados(resultados, self.JornadaActual);
        $("#loading").hide();
    }

    self.ObtenerResultadoGrupo = function () {
        $("#loading").show();
        obtener_resultados_grupo(self.grupo(), self.ObtenerResultadoGrupoCallback);
    }

    self.ObtenerResultadoGrupoCallback = function (resultados) {
        self.CreoObjetoResultados(resultados, self.JornadaAcumulada);
        $("#loading").hide();
    }

    self.CreoObjetoResultados = function(resultados, tipo)
    {
        var _los_resultados = [];
        if (resultados != null) {
            _los_resultados = resultados.resultados;
        }

        tipo(_los_resultados);
    }

    self.BuscarDato = function (data, src) {

    }
}