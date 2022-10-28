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

@app.route("/deletar/<string:classe>", methods=["POST"])
@jwt_required()
def deletar(classe: str):
    # resposta = {"resultado": "ok"}
    detalhes = "ok"

    # Procura o usuário
    currentUser = get_jwt_identity()
    print("Usuário que acessou:", currentUser)

    if not classe.lower() in classes.keys():
        detalhes = f"Classe {classe} não encontrada"
    else:
        # Pega dados
        dados = request.get_json()
        if not "id" in dados:
            detalhes = "ID não incluso"
        else:
            query = db.session.query(classes[classe.lower()]).filter(classes[classe.lower()].id == dados["id"])
            print(query.first())
            if query.first() is None:
                detalhes = f"Objeto do tipo {classe} com ID {dados['id']} não encontrado"
            else:
                query.delete()
                db.session.commit()
    
    resposta = jsonify({
        "resposta": "ok" if detalhes == "ok" else "erro",
        "detalhes": detalhes
    })
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta
