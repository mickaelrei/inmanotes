from geral.config import *
from modelos.usuario import *

@app.route("/login", methods=["POST"])
def login():
    resposta = {"resultado": "ok", "detalhes": "ok"}

    # Informações enviadas pelo front-end
    dados = request.get_json(force=True)

    # Verificar login (a fazer)
    query = db.session.query(Usuario).filter(Usuario.email == dados["email"])
    if not query.first():
        # Não existe
        resposta = {
            "resultado": "erro",
            "detalhes": f"Usuário com email \"{dados['email']}\" não encontrado"
        }
    else:
        # Verificar senha
        if query.first().senha != dados["senha"]:
            # Senha incorreta
            resposta = {
                "resultado": "erro",
                "detalhes": f"Senha incorreta"
            }
        else:
            # Senha correta, guardar na sessão
            pass

    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta