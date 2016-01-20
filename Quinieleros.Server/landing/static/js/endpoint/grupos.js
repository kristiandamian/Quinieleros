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