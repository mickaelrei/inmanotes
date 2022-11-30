let ip
let jwt

$(function() {
    ip = sessionStorage.getItem("ip")
    
    jwt = sessionStorage.getItem("JWT")
    if (!jwt) {
        alert("Você não está logado!")
        window.location = `http://${ip}:5000/login`
        return
    }

    console.log(jwt)
    
    // Pega informações do usuário
    url = `http://${ip}:5000/listar/usuario`
    $.ajax({
        url: url,
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        success: createUserMenu,
        error: function () {
            alert("Erro ao pegar informações do usuário, verifique o backend.")
        }
    })

    // Pega notas do usuário
    $.ajax({
        url: `http://${ip}:5000/listar/nota`,
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        success: createNotes,
        error: function () {
            alert("Erro ao pegar notas do usuário, verifique o backend.")
        }
    })

    // Pega listas de tarefa do usuário
    $.ajax({
        url: `http://${ip}:5000/listar/listatarefa`,
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        success: createChecklists,
        error: function () {
            alert("Erro ao pegar listas de tarefa do usuário, verifique o backend.")
        }
    })

})

function createUserMenu(retorno) {
    if (retorno.resultado === "ok") {
        if (retorno.detalhes.length == 0) {
            alert("Usuário não encontrado!")
            return
        }

        let usuario = retorno.detalhes[0]
        console.log(usuario);

        // Inserir valores
        $("#userName").text(usuario.nome)

        if (usuario.foto != "") {
            $("#userImage").attr("src", usuario.foto)
        }
    } else {
        alert("Erro ao pegar informações do usuário. Detalhes: " + retorno.detalhes)
    }
}

function openProfile() {
    window.location = `http://${ip}:5000/perfil`
}

function logout() {
    // sessionStorage.removeItem("email");
    sessionStorage.removeItem("JWT");

    window.location = `http://${ip}:5000/login`
}

// Funções para criar notas e listas de tarefa na listagem de arquivos
listedNoteHtml = 
`<div class="listedNote" onclick="openFile(this)">
    <img src="static/img/note_icon.png" alt="Note" class="fileIcon"/>
    <p class="listedFileName">nota_1</p>
</div>`

listedChecklistHtml = 
`<div class="listedChecklist" onclick="openFile(this)">
    <img src="static/img/checklist_icon.png" alt="Checklist" class="fileIcon"/>
    <p class="listedFileName">lista_tarefa_1</p>
</div>`

function createListedNote(notaObj) {
    // Criar div padrão de nota
    div = `<div class="listedNote" onclick="openFile(this)">
            <img src="static/img/note_icon.png" alt="Note" class="fileIcon"/>
            <p class="listedFileName">${notaObj.nome}</p>
        </div>`

    $("#filesNav").append(div)
}

function createListedChecklist(checklistObj) {
    // Criar div padrão de lista de tarefa
    div = `<div class="listedChecklist" onclick="openFile(this)">
            <img src="static/img/checklist_icon.png" alt="Checklist" class="fileIcon"/>
            <p class="listedFileName">${checklistObj.nome}</p>
        </div>`

    $("#filesNav").append(div)
}

function createNotes(retorno) {
    if (retorno.resultado === "ok") {
        for (let nota of retorno.detalhes) {
            createListedNote(nota)
        }
    } else {
        alert("Erro ao pegar notas do usuário. Detalhes: " + retorno.detalhes)
    }
}

function createChecklists(retorno) {
    if (retorno.resultado === "ok") {
        for (let nota of retorno.detalhes) {
            createListedChecklist(nota)
        }
    } else {
        alert("Erro ao pegar listas de tarefa do usuário. Detalhes: " + retorno.detalhes)
    }
}

function openFile(obj) {
    console.log(obj)
}