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

    // Conecta clicks de botões
    $("#createNote").on("click", function() {
        // Cria um objeto nota com valores padrões
        let nota = JSON.stringify({
            titulo: "Nova nota",
            conteudo: "Digite algo!"
        })

        // Chama o backend
        $.ajax({
            url: `http://${ip}:5000/inserir/nota`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            headers: { Authorization: 'Bearer ' + jwt},
            data: nota,
            success: function(retorno) {
                if (retorno.resultado === "ok") {
                    // Save in list
                    let note = retorno.detalhes
                    console.log("Saving on id " + note.id)
                    notes[note.id] = note

                    // Add to listed files and open it
                    let listedNoteDiv = createListedNote(note)
                    openFile(listedNoteDiv)
                } else {
                    alert("Falha ao criar nova nota: " + retorno.detalhes)
                }
            },
            error: function(xhr) {
                alert("Erro ao criar nova nota: " + xhr.responseText)
            }
        })
    })

    $("#createChecklist").on("click", function() {
        // Cria um objeto lista de tarefa com valores padrões
        let checklist = JSON.stringify({
            titulo: "Nova lista de tarefas",
        })

        // Chama o backend
        $.ajax({
            url: `http://${ip}:5000/inserir/listatarefa`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            headers: { Authorization: 'Bearer ' + jwt},
            data: checklist,
            success: function(retorno) {
                if (retorno.resultado === "ok") {
                    // Save in list
                    let checklist = retorno.detalhes
                    console.log("Saving on id " + checklist.id)
                    checklists[checklist.id] = checklist

                    // Add to listed files and open it
                    let listedChecklistDiv = createListedChecklist(checklist)
                    openFile(listedChecklistDiv)
                } else {
                    alert("Falha ao criar nova lista de tarefas: " + retorno.detalhes)
                }
            },
            error: function(xhr) {
                alert("Erro ao criar nova lista de tarefas: " + xhr.responseText)
            }
        })
    })
    
    $("#newTask").on("click", function() {
        // Guarda o ID da lista de tarefa aberta
        let id = currentFile.id
        console.log("Adding task on checklist ID=" + id + " | Name=" + checklists[id].titulo)

        // Cria uma tarefa vazia
        let tarefa = JSON.stringify({
            conteudo: "Nova tarefa",
            lista_tarefa_id: id,
        })

        $.ajax({
            url: `http://${ip}:5000/inserir/tarefa`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            headers: { Authorization: 'Bearer ' + jwt},
            data: tarefa,
            success: function(retorno) {
                if (retorno.resultado === "ok") {
                    // Add to checklist
                    let task = retorno.detalhes
                    console.log(task)
                    checklists[id].tarefas.push(task)

                    // Create task div
                    let taskDiv = `<label class="task" id="task_${task.id}">
                    <input ${task.concluido ? "checked" : ""} type="checkbox">
                    <span></span>
                    <textarea spellcheck="false" name="taskEdit" class="taskEdit">${task.conteudo}</textarea>
                    <button class="removeTaskButton" onclick="removeTask(this)">X</button>
                    </label>`

                    $("#tasks").append(taskDiv)
                } else {
                    alert("Falha ao adicionar nova tarefa: " + retorno.detalhes)
                }
            },
            error: function(xhr) {
                alert("Erro ao adicionar nova tarefa: " + xhr.responseText)
            }
        })
    })

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
            alert("Erro ao pegar informações do usuário! faça login novamente.")
            window.location = `http://${ip}:5000/login`
        }
    })
})

function saveFile(file) {
    if (!file)
        return

    if (file.type === "note") {
        // Get JSON obj
        let id = file.id
        let jsonObj = notes[id]

        // Get info
        let titulo = $("#noteTitleEdit").val()
        let conteudo = $("#noteEditArea").val()

        // Check if anything is different
        if (titulo === jsonObj.titulo && conteudo === jsonObj.conteudo) {
            console.log("Nota não modificada")
            return
        }

        let changes = {
            id: id,
            titulo: titulo,
            conteudo: conteudo
        }

        // Create modifications JSON and call backend
        let data = JSON.stringify(changes)
        $.ajax({
            url: `http://${ip}:5000/atualizar/nota`,
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            headers: { Authorization: 'Bearer ' + jwt},
            data: data,
            success: function(retorno) {
                if (retorno.resultado === "ok") {
                    // Updates the object
                    for (let key in changes) {
                        jsonObj[key] = changes[key]
                    }

                    // Update listedFile and openedFile
                    $(`#note_${id}`).find("p").text(titulo)
                    $(`#listed_note_${id}`).find("p").text(titulo)
                } else {
                    alert("Falha ao atualizar: " + retorno.detalhes)
                }
            },
            error: function(xhr) {
                alert("Erro ao atualizar arquivo: " + xhr.responseText)
            }
        })
    } else {
        // Get JSON obj
        let id = file.id
        let jsonObj = checklists[id]

        // Get info
        let titulo = $("#checklistTitleEdit").val()

        // Check if title modified
        if (titulo !== jsonObj.titulo) {
            let changes = {
                id: id,
                titulo: titulo
            }
            let data = JSON.stringify(changes)

            $.ajax({
                url: `http://${ip}:5000/atualizar/listatarefa`,
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                headers: { Authorization: 'Bearer ' + jwt},
                data: data,
                success: function(retorno) {
                    if (retorno.resultado === "ok") {
                        // Updates the object
                        for (let key in changes) {
                            jsonObj[key] = changes[key]
                        }

                        // Update title on listed and opened file divs
                        $(`#checklist_${id}`).find("p").text(titulo)
                        $(`#listed_checklist_${id}`).find("p").text(titulo)
                    } else {
                        alert("Falha ao atualizar lista de tarefa: " + retorno.detalhes)
                    }
                },
                error: function(xhr) {
                    alert("Erro ao atualizar lista de tarefa: " + xhr.responseText)
                }
            })
        }

        // Get tasks
        let taskDivs = $("#tasks").children()
        for (let i = 0; i < taskDivs.length; i++) {
            let taskDiv = $(taskDivs[i])
            let task = jsonObj.tarefas.find(t => t.id == taskDiv.attr("id").split("_")[1])

            // Check if there is a task in this position
            if (task !== undefined) {
                // Check if anything changed
                let concluido = taskDiv.find("input").is(":checked")
                let conteudo = taskDiv.find("textarea").val()

                if (concluido === task.concluido && conteudo === task.conteudo) {
                    console.log("Não modificou")
                    continue
                }

                // Changed, call backend
                let changes = {
                    id: task.id,
                    lista_tarefa_id: jsonObj.id,
                    conteudo: conteudo,
                    concluido: concluido
                }
                let data = JSON.stringify(changes)
                $.ajax({
                    url: `http://${ip}:5000/atualizar/tarefa`,
                    type: 'POST',
                    dataType: 'json',
                    contentType: 'application/json',
                    headers: { Authorization: 'Bearer ' + jwt},
                    data: data,
                    success: function(retorno) {
                        if (retorno.resultado === "ok") {
                            // Updates the object
                            for (let key in changes) {
                                task[key] = changes[key]
                            }
                        } else {
                            alert("Falha ao atualizar tarefa: " + retorno.detalhes)
                        }
                    },
                    error: function(xhr) {
                        alert("Erro ao atualizar tarefa: " + xhr.responseText)
                    }
                })
            } else {
                console.log("No task at ID=" + i)
                console.log(jsonObj)
            }
        }
    }
}

function createUserMenu(retorno) {
    if (retorno.resultado === "ok") {
        if (retorno.detalhes.length == 0) {
            alert("Usuário não encontrado!")
            return
        }

        let usuario = retorno.detalhes[0]
        console.log(usuario)

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
    sessionStorage.removeItem("email")
    sessionStorage.removeItem("JWT")

    window.location = `http://${ip}:5000/login`
}

// Funções para criar notas e listas de tarefa na listagem de arquivos
function createListedNote(notaObj) {
    // Criar div padrão de nota
    div = `<div class="listedNote" id="note_${notaObj.id}" onclick="openFile(this)">
            <img src="static/img/note_icon.png" alt="Note" class="fileIcon"/>
            <p class="listedFileName">${notaObj.titulo}</p>
        </div>`

    $("#filesNav").append(div)

    return document.getElementById(`note_${notaObj.id}`)
}

function createListedChecklist(checklistObj) {
    // Criar div padrão de lista de tarefa
    div = `<div class="listedChecklist" id="checklist_${checklistObj.id}" onclick="openFile(this)">
            <img src="static/img/checklist_icon.png" alt="Checklist" class="fileIcon"/>
            <p class="listedFileName">${checklistObj.titulo}</p>
        </div>`

    $("#filesNav").append(div)

    return document.getElementById(`checklist_${checklistObj.id}`)
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

function changeEditMenu(objType, obj) {
    let titulo = obj.titulo
    // Hide createFileMenu if needed
    if ($("#createFileMenu").css("display") === "block") {
        $("#createFileMenu").css("display", "none")
    }

    // Show correct menu and change content
    if (objType === "note") {
        $("#checklistEditMenu").css("display", "none")
        $("#noteEditMenu").css("display", "block")

        // Change title and text
        $("#noteTitleEdit").val(titulo)
        $("#noteEditArea").val(obj.conteudo)
    } else {
        $("#noteEditMenu").css("display", "none")
        $("#checklistEditMenu").css("display", "block")

        // Change title
        $("#checklistTitleEdit").val(titulo)

        // Clear text
        $("#tasks").empty()

        // Add checkboxes
        for (let i = 0; i < obj.tarefas.length; i++) {
            let task = obj.tarefas[i]
            let taskDiv = `<label class="task" id="task_${task.id}">
            <input ${task.concluido ? "checked" : ""} type="checkbox">
            <span></span>
            <textarea spellcheck="false" name="taskEdit" class="taskEdit">${task.conteudo}</textarea>
            <button class="removeTaskButton" onclick="removeTask(this)">X</button>
            </label>`

            $("#tasks").append(taskDiv)
        }
    }
}

function openFile(divObj) {
    // Get obj type and id
    let sep = divObj.id.split("_")
    let objType, objId
    if (sep.length == 2) {
        objType = sep[0], objId = sep[1]
    } else {
        objType = sep[1], objId = sep[2]
    }
    
    // Check if this file is already open
    for (let file of openedFiles) {
        if (file.type == objType && file.id == objId) {
            // Already open, just switch tabs
            console.log("Already open")
            switchFile(divObj)
            return
        }
    }
    
    // Save current file
    saveFile(currentFile)

    // Unselect last selected file
    if (currentFile !== undefined) {
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
    let objName = obj.titulo
    let openedFileDiv = `<div class="openedFile selectedFile" onclick="switchFile(this)" id="listed_${objType}_${objId}">` +
    `<img src="static/img/${objType}_icon.png" alt="" class="openedFileIcon">` +
    `<p class="fileName">${obj.titulo}</p>` +
    `<button class="fileCloseButton" onclick="closeFile(this)">X</button>` +
    `</div>`

    // Add div to openedFiles div
    $("#filesMenu").append(openedFileDiv)

    // Change UI
    changeEditMenu(objType, obj)

    // Change current file
    currentFile = {type: objType, id: objId}
    openedFiles.push(currentFile)
}

function switchFile(divObj) {    
    // Get obj type and id
    let sep = divObj.id.split("_")
    let objType, objId
    if (sep.length == 2) {
        objType = sep[0], objId = sep[1]
    } else {
        objType = sep[1], objId = sep[2]
    }

    // Check if this isn't the current file
    if (currentFile.type == objType && currentFile.id == objId) {
        console.log("Same file")
        return
    }

    // Save current file before switching files
    saveFile(currentFile)

    // Get JSON obj
    let obj
    if (objType == "checklist") {
        obj = checklists[objId]
    } else {
        obj = notes[objId]
    }

    // Remove selectedFile class from currentFile
    $(`#listed_${currentFile.type}_${currentFile.id}`).removeClass("selectedFile")
    
    // Add selectedFile class to current file
    $(`#listed_${objType}_${objId}`).addClass("selectedFile")

    // Change UI
    changeEditMenu(objType, obj)
    
    // Set new currentFile
    currentFile = {type: objType, id: objId}
}

function closeFile(divObj) {
    console.log("Closing file:")

    // Get the JSON obj
    let div = $(divObj).parent()
    let divId = div.attr("id")
    console.log("id: " + divId)
    let sep = divId.split("_")
    let objType = sep[1], objId = sep[2]

    let obj
    if (objType === "note") {
        obj = notes[objId]
    } else {
        obj = checklists[objId]
    }

    // Save 
    saveFile({type: objType, id: objId})

    // Remove listed file div and item from list
    div.remove()
    openedFiles.pop()

    // Check if this is the only file open
    if (openedFiles.length === 0) {
        console.log("closing")
        // Show createFIleMenu
        $("#createFileMenu").css("display", "block")

        // Hide file edit menu
        $("#noteEditMenu").css("display", "none")
        $("#checklistEditMenu").css("display", "none")
    }

    if (currentFile.type === objType && currentFile.id === objId) {
        // Open the last file in the openedFiles list
        let lastFile = openedFiles[openedFiles.length-1]
        let fileDiv = document.getElementById(`${lastFile.type}_${lastFile.id}`)
        console.log("Opening last file")
        console.log(fileDiv)
        openFile(fileDiv)
    }
}

function removeTask(button) {
    // Get the task
    let taskDiv = $(button).parent()
    let checklist = checklists[currentFile.id]
    let task = checklist.tarefas.find(t => t.id == taskDiv.attr("id").split("_")[1])

    let data = JSON.stringify({
        id: task.id,
        lista_tarefa_id: checklist.id,
    })

    // Call backend to delete
    $.ajax({
        url: `http://${ip}:5000/deletar/tarefa`,
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        headers: { Authorization: 'Bearer ' + jwt},
        data: data,
        success: function(retorno) {
            if (retorno.resultado === "ok") {
                // Delete div and object from list
                taskDiv.remove()
                checklist.tarefas.splice(checklist.tarefas.findIndex(t => t.id === task.id), 1)
            } else {
                alert("Falha ao deletar tarefa: " + retorno.detalhes)
            }
        },
        error: function(xhr) {
            alert("Erro ao deletar tarefa: " + xhr.responseText)
        }
    })
}

function autoGrow(element) {
    element.style.height = "5px";
    element.style.height = (element.scrollHeight)+"px";
}

// Save the file every some seconds
setInterval(function() {
    saveFile(currentFile)
}, 1500)

// Save current file when the window closes
$(window).on("beforeunload", function() {
    saveFile(currentFile)
    return "Salvando arquivo atual..."
})