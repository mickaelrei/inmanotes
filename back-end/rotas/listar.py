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

classes = {
    "nota": Nota,
    "tarefa": Tarefa,
    "listatarefa": ListaTarefa,
    "cargo": Cargo,
    "usuario": Usuario
}

@app.route("/listar/<string:classe>")
def listar(classe: str):
    resposta = {"resultado": "ok"}

    if not classe.lower() in classes.keys():
        resposta.update({
            "resultado": "erro",
            "detalhes": "Classe não encontrada"
        })
    else:
        dados = [p.json() for p in db.session.query(classes[classe.lower()]).all()]
        resposta.update({"detalhes": dados})
    
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta
