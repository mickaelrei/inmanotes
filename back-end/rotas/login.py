from geral.config import *

@app.route("/login", methods=["POST"])
def login():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    # Informações enviadas pelo front-end
    dados = request.get_json(force=True)
    login = dados['login']
    senha = dados['senha']

    # Verificar login (a fazer)

    # if login == 'mylogin' and senha == '123':
    #     # armazenar sessão, para informar que há login realizado
    #     session[login] = "OK"
    # else:
    #     resposta = jsonify({"resultado": "erro", "detalhes": "login e/ou senha inválido(s)"})        

    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir o envio dos cookies
    resposta.headers.add('Access-Control-Allow-Credentials', 'true')
    return resposta  # responder!