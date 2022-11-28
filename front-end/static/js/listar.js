$(function() {
    ip = sessionStorage.getItem("ip")

    // Verificar se está logado
    if (sessionStorage.getItem("JWT") === null) {
        alert("Você não está logado!")
        window.location = "login.html"
    }

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

        if (nomeClasse == "") {
            alert("Digite o nome de uma classe!")
            return
        }

        // Pega o JWT
        let jwt = sessionStorage.getItem("JWT")
        console.log(jwt);
        if (!jwt) {
            alert("Você não está logado!")
            window.location = "login.html"
        }

        $.ajax({
            url: `http://${ip}:5000/listar/${nomeClasse}`,
            method: 'GET',
            dataType: 'json',
            contentType: 'application/json',
            headers: { Authorization: 'Bearer ' + jwt},
            success: listar,
            error: function () {
                alert("Erro ao listar, verifique o backend.")
            }
        })
    })
})

function listar(retorno) {
    console.log("Listando");
    if (retorno.resultado === "ok") {
        if (retorno.detalhes.length == 0) {
            alert("Nenhum objeto retornado")
            return
        }
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
            lin += "</tr>"

            $("#tabelaListarCorpo").append(lin)
        }
    } else {
        alert("Erro ao listar: " + retorno.detalhes)
    }
}