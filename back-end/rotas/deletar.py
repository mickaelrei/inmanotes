# Importar config e classes
from geral.config import *
from modelos.nota import Nota
from modelos.tarefa import Tarefa
from modelos.lista_tarefa import ListaTarefa
from modelos.cargo import Cargo
from modelos.usuario import Usuario

classes = {
    "nota": Nota,
    "tarefa": Tarefa,
    "listatarefa": ListaTarefa,
    "cargo": Cargo,
    "usuario": Usuario
}

def verificaAcesso(classe: str, dados: dict, obj, user_id: int):
    usuario = Usuario.query.filter_by(id=user_id).first()
    cargo = Cargo.query.filter_by(id=usuario.cargo_id).first()

    detalhes = "ok"
    # Verifica se é um administrador
    if cargo.nome == "administrador":
        return detalhes

    if classe.lower() in ("nota", "listatarefa") and obj.usuario_id != user_id:
        detalhes = f"Objeto do tipo {classe} com ID {dados['id']} não pertence ao usuário com ID {user_id}"
    elif classe.lower() == "tarefa":
        # Verifica se pertence a uma lista de tarefa deste usuário
        lista_tarefa = ListaTarefa.query.filter_by(id=obj.lista_tarefa_id).first()
        if not (lista_tarefa and lista_tarefa.usuario_id == user_id):
            detalhes = f"Tarefa com ID {obj.id} pertence à lista com ID {lista_tarefa.id}, que não pertence ao usuário com ID {user_id}"
    elif classe.lower() == "usuario":
        if dados["id"] != user_id:
            detalhes = f"Tentativa de modificar outro usuário (ID logado: {user_id}, ID de tentativa: {dados['id']}"
        
    return detalhes

@app.route("/deletar/<string:classe>", methods=["POST"])
@jwt_required()
def deletar(classe: str):
    detalhes = "ok"

    # Procura o usuário
    email = get_jwt_identity()
    user_id = Usuario.query.filter_by(email=email).first().id

    if not classe.lower() in classes.keys():
        detalhes = f"Classe {classe} não encontrada"
    else:
        # Pega dados
        dados = request.get_json()
        if not "id" in dados:
            detalhes = "ID não incluso"
        else:
            query = db.session.query(classes[classe.lower()]).filter(classes[classe.lower()].id == dados["id"])
            if query.first() is None:
                detalhes = f"Objeto do tipo {classe} com ID {dados['id']} não encontrado"
            else:
                detalhesAcesso = verificaAcesso(classe, dados, query.first(), user_id)
                if detalhesAcesso == "ok":
                    query.delete()
                    db.session.commit()
                else:
                    detalhes = detalhesAcesso
    
    resposta = jsonify({
        "resposta": "ok" if detalhes == "ok" else "erro",
        "detalhes": detalhes
    })
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta
