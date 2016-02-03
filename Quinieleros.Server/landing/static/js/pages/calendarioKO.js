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
        if (!data.jornadaAbierta) {
            if (data.resultado == res) {
                mostrar = true;
            }
        }
        return mostrar;
    };

    self.GuardarTodos = function () {
        self.save(true);
    }

    self.Guardar = function () {
        self.save(false);
    }

    self.save = function (guardarTodos) {
        $("#loading").show();
        var resultados = self.getResultados();
        funcion = save_resultado;
        if (guardarTodos)
            funcion = save_resultados_todos_grupos;
        funcion(resultados, self.saveCallback);
    }

    self.getResultados = function () {
        var _resultados=[];
        for (var i = 0; i < self.partidos().length; i++) {
            var id = self.partidos()[i].key;
            var resultadoSeleccioando = $("#" + id + " .seleccionado").text();
            var resultadoGrabar;
            switch (resultadoSeleccioando) {
                case "Local":
                    resultadoGrabar = "GANA_LOCAL";
                    break;
                case "Empate":
                    resultadoGrabar = "EMPATE";
                    break;
                case "Visitante":
                    resultadoGrabar = "GANA_VISITANTE";
                    break;
                default:
                    resultadoGrabar = "NO_ESPECIFICADO";
                    break;                
            }
            resultado={};
            resultado.partido = id;
            resultado.resultado = resultadoGrabar;
            _resultados.push(resultado);
        }
        var resultados = {};
        resultados.calendariokey = "";
        resultados.resultados = _resultados;
        resultados.correo = self.usuario();
        resultados.grupo = self.grupo();

        return resultados;
    }
    self.saveCallback = function (resp) {
        $("#loading").hide();
        var msg = "Resultados registrados";
        if (resp.error)
            msg = resp.mensaje;
        
        Materialize.toast(msg, 5000);
    }
}