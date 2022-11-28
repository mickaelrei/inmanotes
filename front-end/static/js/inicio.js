$(function() {
    let ip = sessionStorage.getItem("ip")
    url = `http://${ip}:5000/listar/usuario`

    let jwt = sessionStorage.getItem("JWT")
    if (!jwt) {
        alert("Você não está logado!")
        window.location = "login.html"
        return
    }

    $.ajax({
        url: url,
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        success: criarMenuUsuario,
        error: function () {
            alert("Erro ao listar, verifique o backend.")
        }
    })
})

function criarMenuUsuario(retorno) {
    if (retorno.resultado === "ok") {
        if (retorno.detalhes.length == 0) {
            alert("Usuário não encontrado!")
            return
        }

        let usuario = retorno.detalhes[0]
        console.log(usuario);

        // Inserir valores
        $("#usuarioNome").text(usuario.nome)
        $("#usuarioEmail").text(usuario.email)

        $("#usuarioFoto").append(`<img src=${usuario.foto} alt="Foto">`)
    }
}