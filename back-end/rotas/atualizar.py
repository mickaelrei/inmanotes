# Importar config e classes
from geral.config import *
from modelos.nota import Nota
from modelos.tarefa import Tarefa
from modelos.lista_tarefa import ListaTarefa
from modelos.cargo import Cargo
from modelos.usuario import Usuario
from datetime import datetime

classes = {
    "nota": Nota,
    "tarefa": Tarefa,
    "listatarefa": ListaTarefa,
    "cargo": Cargo,
    "usuario": Usuario
}

campos_modificaveis = {
    "nota": [
        "nome",
        "titulo",
        "conteudo"
    ],
    "tarefa": [
        "conteudo",
        "concluido"
    ],
    "listatarefa": [
        "titulo"
    ],
    "cargo": [],
    "usuario": [
        "nome_usuario",
        "nome_display",
        "foto",
        "senha",
        "cargo_id"
    ],
}

@app.route("/atualizar/<string:classe>", methods=["POST"])
def atualizar(classe: str):
    # resposta = {"resultado": "ok", "detalhes": "ok"}
    detalhes = "ok"

    if not classe.lower() in classes.keys():
        detalhes = f"Classe {classe} não encontrada"
    else:
        # Pega dados
        dados = request.get_json()
        if not "id" in dados:
            detalhes = "ID não incluso"
        else:
            obj = classes[classe.lower()].query.get(dados["id"])
            if obj is None:
                detalhes = f"Objeto do tipo {classe} com ID {dados['id']} não encontrado"
            else:
                # Atualiza os campos necessários
                sucesso = True
                for campo, novoDado in dados.items():
                    # Não atualizar o ID
                    if campo == "id": continue

                    # Verifica se esse campo pode ser modificado
                    if hasattr(obj, campo):
                        if campo in campos_modificaveis[classe.lower()]:
                            # Atualiza o campo
                            obj.__setattr__(campo, novoDado)
                        else:
                            detalhes = f"Não é possível modificar o campo {campo} para objetos do tipo {classe}"
                            sucesso = False
                            break
                    else:
                        detalhes = f"Objeto do tipo {classe} não possui campo {campo}"
                        sucesso = False
                        break

                if sucesso:
                    db.session.commit()
    
    resposta = jsonify({
        "resposta": "ok" if detalhes == "ok" else "erro",
        "detalhes": detalhes
    })
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta