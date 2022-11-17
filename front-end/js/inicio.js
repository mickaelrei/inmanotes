$(function() {
    let ip = sessionStorage.getItem("ip")
    url = `http://${ip}:5000/listar/usuario`

    let jwt = sessionStorage.getItem("JWT")
    if (!jwt) {
        alert("Você não está logado!")
        window.location = "login.html"
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
        // Pegar valores na sessão
        var nome = ""
        var email = ""
        var foto = ""

        // Inserir valores
        $("#usuarioNome").val(usuario.nome)
        $("#usuarioEmail").val(usuario.email)

        $("#usuarioFoto").append(`<img src=${usuario.foto} alt=Foto>`)
    }
}