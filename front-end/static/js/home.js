$(function() {
    let ip = sessionStorage.getItem("ip")
    $("#abrirRegistrar").on("click", function() {
        window.location = `http://${ip}:5000/registrar`
    })
})