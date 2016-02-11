get_grupo_byUser = function (usuario, callback) {
    gapi.client.quinieleros.obtener_grupos_del_usuario(
        {
            "grupoKey": usuario
        }).execute(function (resp) {
            var data = resp.result != undefined ? resp.result.grupos : null;
            console.log(data);
            if (callback)
                callback(data);
        });
}

get_grupo = function (grupoKey, callback) {
    gapi.client.quinieleros.obtener_grupo({
        "grupoKey": grupoKey
    }).execute(function (resp) {
        var data = resp.result != undefined ? resp.result : null;
        console.log(data);
        if (callback)
            callback(data);
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

invite_people = function (usuarios, grupo, callback) {
    gapi.client.invite_people({
        "usuarios": usuarios,
        "grupo": grupo
    }).execute(function (resp) {
        console.log(resp.result);
        if (callback)
            callback(resp.result);
    });
}