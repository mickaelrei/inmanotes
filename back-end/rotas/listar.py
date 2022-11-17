# Importar config e classes
from geral.config import *
from modelos.nota import Nota
from modelos.tarefa import Tarefa
from modelos.lista_tarefa import ListaTarefa
from modelos.cargo import Cargo
from modelos.usuario import Usuario

classes = {
    "nota": Nota,
    "listatarefa": ListaTarefa,
    "tarefa": Tarefa,
    "cargo": Cargo,
    "usuario": Usuario
}

def pegarDados(classeNome: str, user_id: int):
    if classeNome in ("nota", "listatarefa"):
        # Pega todos os objetos com id de usuário dado
        dados = [o.json() for o in classes[classeNome].query.filter_by(usuario_id=user_id).all()]
    elif classeNome == "tarefa":
        # Pega todas as tarefas dentro de uma lista de tarefa com o id de usuário dado
        dados = []
        for tarefa in db.session.query(Tarefa).all():
            # Verifica se a lista de tarefa tem o mesmo usuário de id
            lista_tarefa = ListaTarefa.query.filter_by(id=tarefa.lista_tarefa_id).first()
            if lista_tarefa and lista_tarefa.usuario_id == user_id:
                dados.append(tarefa.json())
    elif classeNome == "cargo":
        # Pega todos os cargos
        dados = [o.json() for o in db.session.query(Cargo).all()]
    else:
        # Pega o objeto deste usuário
        usuario = Usuario.query.filter_by(id=user_id).first()
        if usuario:
            dados = [usuario.json()]
        else:
            dados = []

    return dados

@app.route("/listar/<string:classe>")
@jwt_required()
def listar(classe: str):
    resposta = {"resultado": "ok"}


    if not classe.lower() in classes.keys():
        resposta.update({
            "resultado": "erro",
            "detalhes": "Classe nao encontrada"
        })
    else:
        # Pega o ID de usuário
        email = get_jwt_identity()
        user_id = Usuario.query.filter_by(email=email).first().id
        dados = pegarDados(classe.lower(), user_id)
        
        resposta.update({"detalhes": dados})
    
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta