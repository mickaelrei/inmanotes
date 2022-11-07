$(function() {
    ip = sessionStorage.getItem("ip")
    
    // Valores padrão pro register
    $("#campoEmailRegistrar").val("mickael.reichert@gmail.com")
    $("#campoNomeRegistrar").val("Mickael Reichert")
    $("#campoFotoRegistrar").val("")
    $("#campoSenhaRegistrar").val("senhaforte123")

    // Botão de registrar
    $("#botaoRegistrar").click(function() {
        // Pega informações do form
        let email = $("#campoEmailRegistrar").val()
        let nome = $("#campoNomeRegistrar").val()
        let foto = $("#campoFotoRegistrar").val()
        let senha = $("#campoSenhaRegistrar").val()

        // Dados
        let dados = JSON.stringify({
            email: email,
            nome: nome,
            foto: foto,
            senha: senha
        })

        $.ajax({
            url: `http://${ip}:5000/registrar`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: registrarOk,
            error: function () {
                alert("Erro ao registrar, verifique o backend.")
            }
        })
    })
})

function registrarOk(retorno) {
    if (retorno.resultado == "ok") {
        alert("Sucesso ao registrar!")
    } else {
        alert("Erro ao registrar: " + retorno.detalhes)
    }
} 