from geral.config import *
from modelos.usuario import *
from modelos.cargo import *
from datetime import datetime

camposNecessarios = [
    "email",
    "nome",
    "foto",
    "senha"
]

# Pegar ID de usuário comum e administrador
usuarioID = db.session.query(Cargo).filter(Cargo.nome == "usuario").first().id
administradorID = db.session.query(Cargo).filter(Cargo.nome == "administrador").first().id

@app.route("/registrar", methods=["POST"])
def registrar():
    resposta = {"resultado": "ok", "detalhes": "ok"}

    # Dados do front-end
    dados: dict = request.get_json(force=True)
    valido = True
    for campo in camposNecessarios:
        if campo not in dados:
            resposta.update({
                "resultado": "erro",
                "detalhes": f"Campo {campo} não encontrado."
            })
            valido = False
            break
    if valido:
        # Verificar se não existe nenhum usuário com esse e-mail
        busca = db.session.query(Usuario).filter(Usuario.email == dados["email"])
        if busca.first():
            # Existe
            resposta.update({
                "resultado": "erro",
                "detalhes": f"Usuário com e-mail \"{dados['email']}\" já existe"
            })
        else:
            # Adicionar data de criação e ID de cargo
            dados.update({
                "data_criacao": datetime.today(),
                "cargo_id": usuarioID,
            })

            # Adicionar à lista de usuários
            try:
                usuario = Usuario(**dados)
                db.session.add(usuario)
                db.session.commit()
            except TypeError as e:
                resposta.update({
                    "resultado": "erro",
                    "detalhes": str(e)
                })

    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta