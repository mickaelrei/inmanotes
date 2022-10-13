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