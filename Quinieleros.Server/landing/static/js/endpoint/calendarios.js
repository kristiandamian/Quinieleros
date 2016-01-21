get_calendarios = function (liga, callback) {
    gapi.client.quinieleros.obtener_calendarios_de_una_liga({
            "grupoKey": liga
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result.calendarios : null;
        console.log(data);
        if (callback)
            callback(data);
    });
}