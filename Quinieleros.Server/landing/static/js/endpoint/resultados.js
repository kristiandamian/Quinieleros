save_resultado = function (resultados, callback) {
    gapi.client.quinieleros.save_resultados({
        "resultados": resultados
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result : null;
        console.log(data);
        if (callback)
            callback(data);
    });
}

save_resultados_todos_grupos = function (resultados, callback) {
    gapi.client.quinieleros.save_resultados_todos_grupos(
        {
            "resultados": resultados
        }).execute(function (resp) {
            var data = resp.result != undefined ? resp.result : null;
            console.log(data);
            if (callback)
                callback(data);
        });
}

obtener_resultados_grupo = function (grupoKey, callback) {
    gapi.client.quinieleros.obtener_resultados_grupo({
        "grupoKey": grupoKey
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result : null;
        console.log(data);
        if (callback)
            callback(data);
    });
}

obtener_resultados_jornada_grupo = function (grupoKey, callback) {
    gapi.client.quinieleros.obtener_resultados_jornada_grupo({
        "grupoKey": grupoKey
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result : null;
        console.log(data);
        if (callback)
            callback(data);
    });
}