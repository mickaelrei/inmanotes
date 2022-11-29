# Importar config e classes
from geral.config import *
from modelos.nota import Nota
from modelos.tarefa import Tarefa
from modelos.lista_tarefa import ListaTarefa
from modelos.cargo import Cargo
from modelos.usuario import Usuario
from geral.cripto import *

classes = {
    "nota": Nota,
    "listatarefa": ListaTarefa,
    "tarefa": Tarefa,
    "cargo": Cargo,
    "usuario": Usuario
}

def pegarDados(classeNome: str, user_id: int):
    # Verifica se o usuário é administrador
    usuario = Usuario.query.filter_by(id=user_id).first()
    cargo = Cargo.query.filter_by(id=usuario.cargo_id).first()

    if classeNome in ("nota", "listatarefa"):
        if cargo.nome == "administrador":
            # Pega todos os objetos
            query = classes[classeNome].query.all()
        else:
            # Pega todos os objetos com id de usuário dado
            query = classes[classeNome].query.filter_by(usuario_id=user_id).all()
        dados = [o.json() for o in query]
    elif classeNome == "tarefa":
        # Pega todas as tarefas dentro de uma lista de tarefa com o id de usuário dado
        dados = []
        for tarefa in db.session.query(Tarefa).all():
            # Verifica se a lista de tarefa tem o mesmo usuário de id (ou se é um administrador)
            lista_tarefa = ListaTarefa.query.filter_by(id=tarefa.lista_tarefa_id).first()
            if lista_tarefa and lista_tarefa.usuario_id == user_id or cargo.nome == "administardor":
                dados.append(tarefa.json())
    elif classeNome == "cargo":
        # Pega todos os cargos
        dados = [o.json() for o in db.session.query(Cargo).all()]
    else:
        if cargo.nome == "administrador":
            dados = [o.json() for o in Usuario.query.all()]

            # Descriptografa as senhas
            for dado in dados:
                dado["senha"] = decifrar(dado["senha"])
        else:
            # Pega o objeto deste usuário
            dados = [Usuario.query.filter_by(id=user_id).first().json()]

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