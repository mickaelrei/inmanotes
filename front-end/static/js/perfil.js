$(function() {
    // IP e JWT
    let ip = sessionStorage.getItem("ip")
    let jwt = sessionStorage.getItem("JWT")

    if (jwt === undefined) {
        alert("Faça login primeiro!")
        window.localion = `http://${ip}:5000/login`
        return
    }

    $("#editName").on("click", function() {
        // 1) Transformar o <p> em <textarea> ou deixar modificável
        // 2) Esperar input
        // 3) Chamar o backend
        console.log("Edit name")
    })

    $("#editEmail").on("click", function() {
        console.log("Edit email")
    })

    $("#editPassword").on("click", function() {
        console.log("Edit password")
    })

    $.ajax({
        url: `http://${ip}:5000/listar/usuario`,
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        success: setUserInfo,
        error: function (xhr, status, error) {
            success = false
            alert("Erro ao pegar informações do usuário! faça login novamente.")
            window.location = `http://${ip}:5000/login`
        }
    })
})

let user
function setUserInfo(retorno) {
    if (retorno.resultado === "ok") {
        // Set user
        user = retorno.detalhes[0]
        console.log(user)
    
        $("#userName").text(user.nome)
        $("#userEmail").text(user.email)
        $("#userPassword").text("*".repeat(user.senha.length))

        if (user.foto !== "") {
            $("#userIcon").attr("src", user.foto)
        }
    } else {
        alert("Erro ao pegar informações do usuário: " + retorno.detalhes)
    }
}

let isPasswordVisible = false
function togglePasswordVisibility() {
    if (user === undefined) return

    if (isPasswordVisible === true) {
        $("#userPassword").text("*".repeat(user.senha.length))
    } else {
        $("#userPassword").text(user.senha)
    }

    isPasswordVisible = !isPasswordVisible
}