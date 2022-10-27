$(function() {
    // Pegar valores na sessão
    var nome = ""
    var email = ""
    var foto = ""

    // Inserir valores
    $("#usuarioNome").val(nome)
    $("#usuarioEmail").val(email)

    $("#usuarioFoto").append(`<img src=${foto} alt=Foto>`)
})