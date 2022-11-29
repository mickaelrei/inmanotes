$(function() {
    ip = sessionStorage.getItem("ip")

    // Remover o JWT
    console.log("Retirando JWT");
    sessionStorage.removeItem("JWT")
    console.log(sessionStorage.getItem("JWT"));

    // Valores padrão
    // $("#campoEmailLogin").val("mickael.reichert@gmail.com")
    // $("#campoSenhaLogin").val("123senhaforte123")

    // Botão de login
    $("#botaoLogin").click(function() {
        // Pega informações do form
        let email = $("#campoEmailLogin").val()
        let senha = $("#campoSenhaLogin").val()

        // Verifica se o usuário digitou algo nas duas opções
        if (email === "") {
            alert("Digite seu email!")
            return
        } else if (senha === "") {
            alert("Digite sua senha!")
            return
        }

        // Dados
        let dados = JSON.stringify({
            email: email,
            senha: senha
        })

        realizarLogin(dados)
    })

    $("#botaoRegistrarRedirect").click(function() {
        // Redireciona para a página de registrar
        window.location = `http://${ip}:5000/registrar`
    })
})

function loginOk(retorno, email) {
    if (retorno.resultado == "ok") {
        // Guarda o JWT e o login na sessão
        sessionStorage.setItem("email", email)
        sessionStorage.setItem("JWT", retorno.detalhes)

        window.location = `http://${ip}:5000/inicio`
    } else {
        alert("Erro no login: " + retorno.detalhes)
    }
}

function realizarLogin(dados) {
    url = `http://${ip}:5000/loginBack`
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: dados,
        success: function(retorno) {
            loginOk(retorno, dados.email)
        },
        error: function (xhr, status, error) {
            alert(`Erro no login, verifique o backend. ${xhr.responseText} | ${status} | ${error}`)
        }
    })
}