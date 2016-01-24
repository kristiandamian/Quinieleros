﻿/// <reference path="../endpoint/jornadas.js" />

var modeloCalendario = function () {
    var self = this;

    self.grupo = ko.observable();
    self.usuario = ko.observable();
    self.jornadas = ko.observableArray();
    self.partidos = ko.observableArray();

    /// FUNCIONES

    self.ObtenerJornadas = function () {
        $("#loading").show();
        get_jornadas(self.grupo(), self.ObtenerJornadasCallback);
    }

    self.ObtenerJornadasCallback = function (jornadas) {
        self.jornadas(jornadas);
        
        $("#loading").hide();
        $('ul.tabs').tabs();
        self.ObtengoPartidosApi(self.grupo(), 1, self.usuario());
    }

    self.ObtengoPartidos = function(parent)
    {
        self.ObtengoPartidosApi(self.grupo(), parseInt(parent.Numero), self.usuario());
    }

    self.ObtengoPartidosApi = function (grupo, jornada, usuario)
    {
        $("#loading").show();
        get_jornada(grupo, jornada, usuario, self.ObtengoPartidosApiCallback);
    }

    self.ObtengoPartidosApiCallback = function(jornada)
    {
        if(jornada!=undefined)
        {
            console.log(jornada);
            self.partidos(jornada.partidos);
        }
        $("#loading").hide();
    }

    self.MarcoSeleccionado = function(data, btn)
    {
        
        var _this = $(event.target);
        console.log(data);
        if (data.jornadaAbierta) {
            $(_this).parent().find(".seleccionado").remove();

            var html = '<i class="material-icons imgbotoncard seleccionado">done</i>'
            $(_this).before(html);

            // $($("a")[45]).before('<i class="material-icons imgbotoncard seleccionado">done</i>')
        }
    }

    self.AciertoLocal = function(data,item)
    {
        return self.ResultadosLocal(data, item, "GANA_LOCAL") && data.acierto;
    }
    self.FallaLocal = function (data, item) {
        return self.ResultadosLocal(data, item, "GANA_LOCAL") && !data.acierto;
    }
    self.ResultadosLocal = function (data, item, res) {
        var mostrar = false;
        console.log("--------------------------------------------------");
        console.log("1");
        if (!data.jornadaAbierta) {
            console.log("2");
            if (data.resultado == res) {
                mostrar = true;
            }
        }
        return mostrar;
    };
}