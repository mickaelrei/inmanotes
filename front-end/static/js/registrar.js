$(function() {
    ip = sessionStorage.getItem("ip")

    // Botão de registrar
    $("#botaoRegistrar").click(function() {
        // Pega informações do form
        let email = $("#campoEmailRegistrar").val()
        let nome = $("#campoNomeRegistrar").val()
        let foto = $("#campoFotoRegistrar").val()
        let senha = $("#campoSenhaRegistrar").val()

        // Verifica se o usuário digitou algo nas opções (exceto em foto, pois há uma foto padrão)
        if (email === "") {
            alert("Digite um email!")
            return
        } else if (nome === "") {
            alert("Digite um nome!")
            return
        } else if (senha === "") {
            alert("Digite uma senha!")
            return
        }

        // Dados
        let dados = JSON.stringify({
            email: email,
            nome: nome,
            foto: foto,
            senha: senha
        })

        $.ajax({
            url: `http://${ip}:5000/registrarBack`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: function(retorno) {
                registrarOk(retorno, dados)
            },
            error: function() {
                alert("Erro ao registrar, verifique o backend.")
            }
        })
    })

    $("#botaoLoginRedirect").click(function() {
        // Redireciona para a página de login
        window.location = `http://${ip}:5000/login`
    })
})

function registrarOk(retorno, dados) {
    if (retorno.resultado == "ok") {
        // Realiza login e salva JWT
        $.ajax({
            url: `http://${ip}:5000/loginBack`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: loginResposta,
            error: function (xhr, status, error) {
                alert(`Erro no login, verifique o backend. ${xhr.responseText} | ${status} | ${error}`)
            }
        })

        alert("Sucesso ao registrar!")
        window.location = `http://${ip}:5000/inicio`
    } else {
        alert("Erro ao registrar: " + retorno.detalhes)
    }
}

function loginResposta(retorno) {
    if (retorno.resultado === "ok") {
        sessionStorage.setItem("email", email)
        sessionStorage.setItem("JWT", retorno.detalhes)
    } else {
        alert("Erro ao realizar login após registro de conta! Detalhes: " + retorno.detalhes)
    }
}