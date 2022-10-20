from geral.config import *

@app.route("/registrar", methods=["POST"])
def registrar():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    # Dados do front-end
    dados = request.get_json(force=True)  
    login = dados['login']
    senha = dados['senha']

    # Verificar se não existe nenhum usuário com esse e-mail
    
    # Adicionar à lista de usuários

    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir o envio dos cookies
    resposta.headers.add('Access-Control-Allow-Credentials', 'true')
    return resposta  # responder!