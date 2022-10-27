$(function() {
    // Valores padrão pro login
    $("#campoEmailLogin").val("mickael.reichert@gmail.com")
    $("#campoSenhaLogin").val("senhaforte123")

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

        $.ajax({
            url: `http://localhost:5000/login`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: loginOk,
            error: function () {
                alert("Erro no login, verifique o backend.")
            }
        })
    })
})

function loginOk(retorno) {
    if (retorno.resultado == "ok") {
        alert("Sucesso no login!")
    } else {
        alert("Erro no login: " + retorno.detalhes)
    }
} 