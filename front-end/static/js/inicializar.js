$(function() {
    // IP
    var url = document.URL
    var protocolo = "http://"
    var http = protocolo.length
    var comeco = url.substring(http)
    var partes = comeco.split("/")
    var primeiro = partes[0]

    var meuip
    var posicao_doispontos = primeiro.indexOf(":")
    if (posicao_doispontos >= 0) {
        meuip = primeiro.substring(0, posicao_doispontos)
    } else {
        meuip = primeiro
    }
    console.log("Meu Ip: " + meuip);
    sessionStorage.setItem("ip", meuip)
})