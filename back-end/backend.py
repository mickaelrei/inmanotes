from geral.config import *
from rotas.listar import *
from rotas.inserir import *
from rotas.atualizar import *
from rotas.deletar import *

@app.route("/")
def inicio():
    return "Backend operante\n"

app.run(debug=True)