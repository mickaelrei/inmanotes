let ip, jwt, currentFile
let notes = [], checklists = [], openedFiles = []

let query = document.getElementsByClassName("selectedFile")
currentFile = query[0]

$(function() {
    ip = sessionStorage.getItem("ip")
    
    jwt = sessionStorage.getItem("JWT")
    if (!jwt) {
        alert("Você não está logado!")
        window.location = `http://${ip}:5000/login`
        return
    }
    console.log(jwt)

    let success = true
    
    // Pega informações do usuário
    url = `http://${ip}:5000/listar/usuario`
    $.ajax({
        url: url,
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        success: createUserMenu,
        error: function (xhr, status, error) {
            success = false
            alert("Erro usuário! faça login novamente.")
            window.location = `http://${ip}:5000/login`
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
        console.log(usuario.notas)
        console.log(usuario.listas_tarefas)

        // Inserir valores
        $("#userName").text(usuario.nome)

        if (usuario.foto != "") {
            $("#userImage").attr("src", usuario.foto)
        }

        // Cria div de arquivo pra cada nota e lista de tarefa do usuário
        createChecklists(usuario.listas_tarefas)
        createNotes(usuario.notas)
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
function createListedNote(notaObj) {
    // Criar div padrão de nota
    div = `<div class="listedNote" id="note_${notaObj.id}" onclick="openFile(this)">
            <img src="static/img/note_icon.png" alt="Note" class="fileIcon"/>
            <p class="listedFileName">${notaObj.nome}</p>
        </div>`

    $("#filesNav").append(div)
}

function createListedChecklist(checklistObj) {
    // Criar div padrão de lista de tarefa
    div = `<div class="listedChecklist" id="checklist_${checklistObj.id}" onclick="openFile(this)">
            <img src="static/img/checklist_icon.png" alt="Checklist" class="fileIcon"/>
            <p class="listedFileName">${checklistObj.nome}</p>
        </div>`

    $("#filesNav").append(div)
}

function createNotes(notesObj) {
    for (let nota of notesObj) {
        // Salva na lista
        notes[nota.id] = nota
        createListedNote(nota)
    }
}

function createChecklists(checklistsObj) {
    for (let lista of checklistsObj) {
        // Salva na lista
        checklists[lista.id] = lista
        createListedChecklist(lista)
    }
}

function openFile(divObj) {
    // Get type of object (note or checklist) and object id
    let sep = divObj.id.split("_")
    let objType = sep[0], objId = sep[1]

    // Check if this file is already open
    for (let file of openedFiles) {
        if (file.type == objType && file.id == objId) {
            console.log("Already opened file")
            // Already open, just switch tabs
            switchFile(divObj)
            return
        }
    }

    // Unselect last selected file
    if (currentFile !== undefined) {
        console.log("Switching selected file")
        let currentListedFileId = `#listed_${currentFile.type}_${currentFile.id}`
        $(currentListedFileId).removeClass("selectedFile")
    }

    // Get JSON obj
    let obj
    if (objType == "checklist") {
        obj = checklists[objId]
    } else {
        obj = notes[objId]
    }

    // Create a openedFile div
    let objName = obj.nome
    let openedFileDiv = `<div class="openedFile selectedFile" onclick="switchFile(this)" id="listed_${objType}_${objId}">` +
    `<img src="static/img/${objType}_icon.png" alt="" class="openedFileIcon">` +
    `<p class="fileName">${objName}</p>` +
    `<button class="fileCloseButton" onclick="closeFile(this)">X</button>` +
    `</div>`

    // Add div to openedFiles div
    $("#filesMenu").append(openedFileDiv)

    // Check if create file menu is visible (no files opened yet)
    if ($("#createFileMenu").css("display") === "block") {
        // Hide create file menu
        $("#createFileMenu").css("display", "none")
    }

    // Show correct type of edit menu
    if (currentFile !== undefined && currentFile.type !== objType) {
        $(`#${currentFile.type}EditMenu`).css("display", "none")
    }

    $(`#${objType}EditMenu`).css("display", "block")

    // Change current file
    currentFile = {type: objType, id: objId}
    openedFiles.push(currentFile)
}

function closeFile(divObj) {
    console.log("Closing file:")
    console.log(divObj)

    if (currentFile === divObj) {

    }
}

function switchFile(divObj) {
    console.log("Switching file")
    // Remove selectedFile class from currentFile

    // Get new JSON obj from this div

    // Set new currentFile

    // Change edit menu if needed

    // Add selectedFile class to this div
}

function autoGrow(element) {
    element.style.height = "5px";
    element.style.height = (element.scrollHeight)+"px";
}