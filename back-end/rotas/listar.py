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
@jwt_required()
def listar(classe: str):
    resposta = {"resultado": "ok"}

    # Procura o usuário
    currentUser = get_jwt_identity()
    print("Usuário que acessou:", currentUser)

    if not classe.lower() in classes.keys():
        resposta.update({
            "resultado": "erro",
            "detalhes": "Classe nao encontrada"
        })
    else:
        dados = [p.json() for p in db.session.query(classes[classe.lower()]).all()]
        resposta.update({"detalhes": dados})
    
    resposta = jsonify(resposta)
    resposta.headers.add("Access-Control-Allow-Origin", "*")

    return resposta

''''

Testes:

1) Realizar login

curl localhost:5000/login -X POST -H "Content-Type:application/json" -d "{\"email\": \"mickael.reichert@gmail.com\", \"senha\": \"123senhaforte123\"}"
{
  "detalhes": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NjkxODk0MSwianRpIjoiNTdjNmVmMjUtNDA3Ny00MDRiLWJmNWMtN2M4ZmQ0ZDRkZjM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1pY2thZWwucmVpY2hlcnRAZ21haWwuY29tIiwibmJmIjoxNjY2OTE4OTQxLCJleHAiOjE2NjY5MTk1NDF9.DF-K7KpYUD2HzGQOngmaZdXP1nJXXBw5MShZESBE7Bw",
  "resultado": "ok"
}

2) Utilizar JWT na rota

curl localhost:5000/listar/nota -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NjkxODk0MSwianRpIjoiNTdjNmVmMjUtNDA3Ny00MDRiLWJmNWMtN2M4ZmQ0ZDRkZjM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im1pY2thZWwucmVpY2hlcnRAZ21haWwuY29tIiwibmJmIjoxNjY2OTE4OTQxLCJleHAiOjE2NjY5MTk1NDF9.DF-K7KpYUD2HzGQOngmaZdXP1nJXXBw5MShZESBE7Bw"
{
  "detalhes": [
    {
      "conteudo": "testando classe nota. Texto base",
      "data_criacao": "Wed, 26 Oct 2022 21:24:46 GMT",
      "id": 1,
      "nome": "teste",
      "titulo": "Testando",
      "usuario_id": 1
    }
  ],
  "resultado": "ok"
}

'''