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

camposObrigatorios = {
    "nota": [
        "titulo",
        "conteudo",
    ],
    "tarefa": [
        "conteudo",
        "lista_tarefa_id"
    ],
    "listatarefa": [
        "titulo",
    ],
    "cargo": [
        "nome",
        "descricao"
    ],
    "usuario": [
        "nome",
        "foto",
        "senha",
        "cargo_id"
    ]
}

def verificarDados(classe: str, dados: dict, user_id: int=None) -> str:
    '''
    Verifica os dados e caso não estiver correto, retorna uma string com os detalhes
    '''

    if classe in ("nota", "lista_tarefa"):
        query = db.session.query(Usuario).filter(Usuario.id == user_id)
        if not query.first():
            return f"Usuário com ID {user_id} não encontrado"
    elif classe == "usuario":
        query = db.session.query(Cargo).filter(Cargo.id == dados["cargo_id"])
        if not query.first():
            return f"Cargo com ID {dados['cargo_id']} não encontrado"
    elif classe == "tarefa":
        query = db.session.query(ListaTarefa).filter(ListaTarefa.id == dados["lista_tarefa_id"])
        if not query.first():
            return f"Lista de Tarefa com ID {dados['lista_tarefa_id']} não encontrado"
        # Verifica se essa lista é do usuário
        elif query.first().usuario_id != user_id:
            return f"A lista de tarefas de ID {dados['lista_tarefa_id']} não pertence ao usuário de ID {user_id}"

    return "ok"


@app.route("/inserir/<string:classe>", methods=["POST"])
@jwt_required()
def inserir(classe: str):
    resposta = {"resultado": "ok", "detalhes": "ok"}

    if not classe.lower() in classes.keys():
        resposta.update({
            "resultado": "erro",
            "detalhes": "Classe nao encontrada"
        })
    else:
        # Pega dados
        dados = request.get_json(force=True)

        # Verifica se possui todos os campos obrigatórios
        sucesso = True
        for campo in camposObrigatorios[classe.lower()]:
            if campo not in dados:
                resposta.update({
                    "resultado": "erro",
                    "detalhes": f"Classe {classe.lower()} necessita do campo {campo}"
                })
                sucesso = False
                break
        
        if sucesso:
            # Verifica se os dados de referência a outras classes são válidos
            email = get_jwt_identity()
            user = Usuario.query.filter_by(email=email).first()
            resultado = verificarDados(classe.lower(), dados, user.id)
            if resultado != "ok":
                resposta.update({
                    "resultado": "erro",
                    "detalhes": resultado
                })
            else:
                # Adicionar data atual para notas e listas de tarefa
                if classe.lower() in ("nota", "listatarefa", "usuario"):
                    dados.update({"data_criacao": datetime.now()})

                # Converter campo "concluido" para booleano
                if classe.lower() == "tarefa":
                    if "concluido" in dados:
                        if type(dados['concluido']) != bool:
                            dados.update({"concluido": True if dados["concluido"] == "true" else False})
                    else:
                        dados.update({"concluido": False})

                # Adiciona o campo usuario_id nas notas e listas de tarefa
                if classe.lower() in ("nota", "listatarefa"):
                    dados.update({"usuario_id": user.id})

                # Tenta adicionar ao banco de dados
                try:
                    obj = classes[classe](**dados)
                    db.session.add(obj)
                    db.session.commit()

                    # Atualizar resposta
                    resposta.update({"detalhes": obj.json()})
                except TypeError as e:
                    # Em caso de erro, atualiza a resposta
                    resposta.update({
                        "resultado": "erro",
                        "detalhes": str(e)
                    })
    
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta