from geral.config import *
from rotas.listar import *

@app.route("/")
def inicio():
    return "Backend operante\n"

app.run(debug=True)

'''

Diagramas UML código:

@startuml

title InMaNotes


class Nota {
  +DateTime data_criacao
  +String nome
  +String titulo
  +String conteudo
  +Usuario usuario
}

class Tarefa {
  +String conteudo
  +Bool concluido
  +ListaTarefa lista_tarefa
}

class ListaTarefa {
  +String titulo
  +List of Tarefa tarefas
  +Usuario usuario
}

class Usuario {
  +String nome_usuario
  +String nome_display
  +String senha
  +String foto
  +Cargo cargo
}

class Cargo {
  +String nome
}

ListaTarefa *-- Tarefa
Usuario *-- ListaTarefa
Usuario *-- Nota
Usuario o-- Cargo

@enduml




'''