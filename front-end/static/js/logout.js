$(function() {
    // Botão de logout
    $("#botaoLogout").click(function() {
        sessionStorage.removeItem("email");
        sessionStorage.removeItem("JWT");

        window.location = `http://${ip}:5000/login`
    })
})