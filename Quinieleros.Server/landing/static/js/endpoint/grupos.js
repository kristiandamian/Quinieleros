get_grupo_byUser = function (usuario, callback) {
    gapi.client.quinieleros.obtener_grupos_del_usuario(
        {
            "grupoKey": usuario
        }).execute(function (resp) {
            console.log(resp.result.grupos);
            if (callback)
                callback(resp.result.grupos);
        });
}

save_grupo = function (nombre, usuarios, calendario, callback) {
    gapi.client.save_grupo({
        "Nombre": nombre,
        "usuarios":usuarios,
       "calendarioKey":calendario
    }).execute(function (resp) {
        console.log(resp.result);
        if (callback)
            callback(resp.result);
    });
}