get_ligas = function (callback) {
    gapi.client.quinieleros.obtener_todas_las_ligas({
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result.ligas : null;
        console.log(data);
        if (callback)
            callback(data);
    });
}