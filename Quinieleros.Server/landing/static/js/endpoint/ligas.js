get_ligas = function (callback) {
    gapi.client.quinieleros.obtener_todas_las_ligas({
    }).execute(function (resp) {
            console.log(resp.result.ligas);
            if (callback)
                callback(resp.result.ligas);
        });
}