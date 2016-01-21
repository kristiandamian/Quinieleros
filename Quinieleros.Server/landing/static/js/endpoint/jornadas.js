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