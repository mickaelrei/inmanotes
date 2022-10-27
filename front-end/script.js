$(function() {
    // Valores padrão pro register
    $("#campoEmailRegistrar").val("mickael.reichert@gmail.com")
    $("#campoNomeRegistrar").val("Mickael Reichert")
    $("#campoFotoRegistrar").val("")
    $("#campoSenhaRegistrar").val("senhaforte123")

    // Quando apertar enter no input de nome de classe, ativar o click do botão de listar
    $("#nomeClasse").keyup(function(event) {
        if (event.key == "Enter") {
            $("#botaoListar").click()
        }
    })

    // Listar objetos
    $("#botaoListar").click(function() {
        // Pega o nome da classe
        let nomeClasse = $("#nomeClasse").val()
        // let nomeClasse = "nota"

        if (nomeClasse == "") {
            alert("Digite o nome de uma classe!")
            return
        }

        $.ajax({
            url: `http://localhost:5000/listar/${nomeClasse}`,
            method: 'GET',
            success: listar,
            error: function () {
                alert("Erro, verifique o backend.")
            }
        })
    })

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
            url: `http://localhost:5000/registrar`,
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

function listar(retorno) {
    if (retorno.resultado == "ok") {
        // Limpa o cabeçalho
        $("#tabelaListarCabecalho").empty()

        // Cria colunas pro cabeçalho
        for (let key of Object.keys(retorno.detalhes[0])) {
            let lin = `<th class="text-left">${key}</th>`

            $("#tabelaListarCabecalho").append(lin)
        }

        // Limpa o corpo da tabela
        $("#tabelaListarCorpo").empty()

        // Cria linhas pra cada entrada da lista
        for (let obj of retorno.detalhes) {
            let lin = "<tr>"
            for (let key of Object.keys(retorno.detalhes[0])) {
                if (typeof obj[key] == "object") {
                   lin += `<td class="text-left">[Objeto]</td>`
                   continue
                }

                lin += `<td class="text-left">${obj[key]}</td>`
            }
            // let lin = `<tr>
            //     <td>${nota.id}</td>
            //     <td>${nota.data_criacao}</td>
            //     <td>${nota.nome}</td>
            //     <td>${nota.titulo}</td>
            //     <td>${nota.conteudo}</td>
            //     <td>${nota.usuario_id}</td>
            lin += "</tr>"

            $("#tabelaListarCorpo").append(lin)
        }
    } else {
        alert("Erro ao listar: " + retorno.detalhes)
    }
}

function registrarOk(retorno) {
    if (retorno.resultado == "ok") {
        alert("Sucesso ao registrar!")
    } else {
        alert("Erro ao registrar: " + retorno.detalhes)
    }
} 