save_resultado = function (resultados, callback) {
    gapi.client.quinieleros.save_resultados({
        "resultados": resultados
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result.calendarios : null;
        console.log(resp.result);
        if (callback)
            callback(resp.result);
    });
}

save_resultados_todos_grupos = function (resultados, callback) {
    gapi.client.quinieleros.save_resultados_todos_grupos(
        {
            "resultados": resultados
        }).execute(function (resp) {
            var data = resp.result != undefined ? resp.result.calendarios : null;
            console.log(resp.result);
            if (callback)
                callback(resp.result);
        });
}