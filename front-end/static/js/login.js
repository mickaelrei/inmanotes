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

        // Dados
        let dados = JSON.stringify({
            email: email,
            senha: senha
        })

        url = `http://${ip}:5000/loginBack`
        console.log(url);
        $.ajax({
            url: url,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: function(retorno) {
                loginOk(retorno, email)
            },
            error: function (xhr, status, error) {
                alert(`Erro no login, verifique o backend. ${xhr.responseText} | ${status} | ${error}`)
            }
        })
    })

    $("#botaoRegistrarRedirect").click(function() {
        // Redireciona para a página de registrar
        window.location = "registrar.html"
    })
})

function loginOk(retorno, email) {
    if (retorno.resultado == "ok") {
        // Guarda o JWT e o login na sessão
        sessionStorage.setItem("email", email)
        sessionStorage.setItem("JWT", retorno.detalhes)
        alert("Sucesso no login!")
        window.location = "inicio.html"
    } else {
        alert("Erro no login: " + retorno.detalhes)
    }
} 