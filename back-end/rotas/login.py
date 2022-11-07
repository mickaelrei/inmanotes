from geral.config import *
from modelos.usuario import *

@app.route("/login", methods=["POST"])
def login():
    # Informações enviadas pelo front-end
    dados = request.get_json(force=True)

    # Verificar login (a fazer)
    usuario = db.session.query(Usuario).filter(Usuario.email == dados["email"]).first()
    if usuario is None:
        # Não existe
        resposta = {
            "resultado": "erro",
            "detalhes": f"Usuário com email \"{dados['email']}\" não encontrado"
        }
    else:
        # Verificar senha
        if usuario.senha != dados["senha"]:
            # Senha incorreta
            resposta = {
                "resultado": "erro",
                "detalhes": f"Senha incorreta."
            }
        else:
            # Senha correta, entregar JWT
            access_token = create_access_token(identity=dados["email"])
            resposta = {
                "resultado": "ok",
                "detalhes": access_token
            }

    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta