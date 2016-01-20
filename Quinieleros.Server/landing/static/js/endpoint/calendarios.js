get_calendarios = function (liga, callback) {
    gapi.client.quinieleros.obtener_calendarios_de_una_liga({
            "grupoKey": liga
    }).execute(function (resp) {
        console.log(resp.result.calendarios);
        if (callback)
            callback(resp.result.calendarios);
    });
}