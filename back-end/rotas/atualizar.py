# from init import *
# Incluir caminhos
import sys
sys.path.append('/home/aluno/inmanotes/back-end')
sys.path.append('/home/aluno/inmanotes/back-end')

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
    resposta = {"resultado": "ok", "detalhes": "ok"}

    if not classe.lower() in classes.keys():
        resposta.update({
            "resultado": "erro",
            "detalhes": "Classe nao encontrada"
        })
    else:
        # Pega dados
        dados = request.get_json()
        if not "id" in dados:
            resposta.update({
                "resultado": "erro",
                "detalhes": "ID não incluso"
            })
        else:
            obj = classes[classe.lower()].query.get(dados["id"])
            if obj is None:
                resposta.update({
                    "resultado": "erro",
                    "detalhes": f"Objeto do tipo {classe.lower()} com ID {dados['id']} não encontrado"
                })
            else:
                for campo, novoDado in dados.items():
                    if campo in campos_modificaveis[classe.lower()]:
                        print(f"Campo: {campo}")
                        obj[campo] = novoDado

                        # NAO SUPORTA ITEM ASSIGNMENT (OBJ[TAL] = TAL)
                db.session.commit()
        
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta