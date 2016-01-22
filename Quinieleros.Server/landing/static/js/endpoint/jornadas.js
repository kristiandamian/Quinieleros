get_jornadas = function (calendario, callback) {
    gapi.client.quinieleros.obtener_jornadas({
        "grupokey": calendario
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result.jornadas : null;
        console.log(data);
        if (callback)
            callback(data);
    });
}

get_jornada = function (grupo,jornada,usuario, callback) {
    gapi.client.quinieleros.obtener_jornada({
        "grupokey": grupo,
        "jornada": jornada,
        "usuario": usuario, 
    }).execute(function (resp) {
        var data = resp.result;
        console.log(data);
        if (callback)
            callback(data);
    });
}