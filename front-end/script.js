$(function() {
    $("#listarNotas").click(function() {
        // Pega o nome da classe
        // let nomeClasse = $("#nomeClasse").val()
        let nomeClasse = "nota"

        $.ajax({
            url: `http://localhost:5000/listar/${nomeClasse}`,
            method: 'GET',
            success: listar, // chama a função listar para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });
    })

    $("#botaoRegistrar").click(function() {
        // Pega informações do form
        let email = $("#campoEmailRegister").val()
        let nome = $("#campoNomeRegister").val()
        let foto = $("#campoFotoRegister").val()
        let senha = $("#campoSenhaRegister").val()

        // Dados
        let dados = JSON.stringify({
            email: email,
            nome: nome,
            foto: foto,
            senha: senha
        })

        console.log(dados);

        $.ajax({
            url: `http://localhost:5000/registrar`,
            type: 'POST', // TESTE COM A OPÇÃO GET no front e no back; observe o log do servidor
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            xhrFields: { withCredentials: true }, // para que os cookies sejam enviados
            success: registrarOk, // chama a função listar para processar o resultado
            error: function (xhr, status, error) {
                alert("Erro na conexão, verifique o backend. " + xhr.responseText + " - " + status + " - " + error);
                // https://api.jquery.com/jquery.ajax/
            }
        });
    })
})

function listar(retorno) {
    if (retorno.resultado == "ok") {
        $("#notas").empty()

        console.log(nomeClasse);
        for (let nota of retorno.detalhes) {
            let lin = `<tr>
                <td>${nota.id}</td>
                <td>${nota.data_criacao}</td>
                <td>${nota.nome}</td>
                <td>${nota.titulo}</td>
                <td>${nota.conteudo}</td>
                <td>${nota.usuario_id}</td>
            </tr>`

            $("#notas").append(lin)
        }
    } else {
        alert("Erro ao listar notas: " + retorno.detalhes)
    }
}

function registrarOk(retorno) {
    if (retorno.resultado == "ok") {
        alert("Sucesso ao registrar!")
    } else {
        alert("Erro ao registrar: " + retorno.detalhes)
    }
}