from geral.config import *
from modelos.usuario import *
from modelos.cargo import *
from geral.cripto import *
from datetime import datetime
import re

camposNecessarios = [
    "email",
    "nome",
    "foto",
    "senha"
]

# Verificação de email
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def emailValido(email: str) -> bool:
    return regex.fullmatch(email) != None

# Pegar ID de usuário comum e administrador
usuarioID = db.session.query(Cargo).filter(Cargo.nome == "usuario").first().id
administradorID = db.session.query(Cargo).filter(Cargo.nome == "administrador").first().id

@app.route("/registrarBack", methods=["POST"])
def registrarBack():
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
            # Verifica se é um email válido
            if not emailValido(dados["email"]):
                resposta.update({
                    "resultado": "erro",
                    "detalhes": f"O email {dados['email']} não é válido"
                })
            else:
                # Adicionar data de criação e ID de cargo
                dados.update({
                    "data_criacao": datetime.today(),
                    "cargo_id": usuarioID,
                })

                # Criptografa senha
                dados.update({"senha": cifrar(dados["senha"])})

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