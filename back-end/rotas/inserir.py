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

@app.route("/inserir/<string:classe>", methods=["POST"])
def inserir(classe: str):
    resposta = {"resultado": "ok", "detalhes": "ok"}

    if not classe.lower() in classes.keys():
        resposta.update({
            "resultado": "erro",
            "detalhes": "Classe nao encontrada"
        })
    else:
        # Pega dados
        dados = request.get_json()

        # Adicionar data atual para notas e listas de tarefa
        if classe.lower() in ("nota", "listatarefa", "usuario"):
            dados.update({"data_criacao": datetime.now()})

        # Converter campo "concluido" para booleano
        if classe.lower() == "tarefa":
            concluido = dados["concluido"]
            print(type(concluido))
            if type(concluido) != bool:
                dados.update({"concluido": True if concluido.lower() == "true" else False})

        # Tenta adicionar ao banco de dados
        try:
            obj = classes[classe](**dados)
            db.session.add(obj)
            db.session.commit()

            # Atualizar resposta
            resposta.update({"detalhes": dados})
        except TypeError as e:
            # Em caso de erro, atualiza a resposta
            resposta.update({
                "resultado": "erro",
                "detalhes": str(e)
            })
    
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta