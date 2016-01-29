var modeloEstadisticas = function () {
    var self = this;
    self.grupo = ko.observable();
    self.usuario = ko.observable();
    self.NombreGrupo = ko.observable();
    self.NombreJornada = ko.observable();
    self.JornadaActual = ko.observableArray();
    self.JornadaAcumulada = ko.observableArray();

    /// FUNCIONES BABY
    self.NombreGrupo = ko.computed(function () {
        return "Estadisticas del grupo " + self.NombreGrupo();
    });
    
    
}