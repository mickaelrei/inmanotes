import sys
# Desativar criação das pastas __pycache__
sys.dont_write_bytecode = True

from geral.config import *
from rotas.listar import *
from rotas.inserir import *
from rotas.atualizar import *
from rotas.deletar import *
from rotas.registrar import *
from rotas.login import *

@app.route("/")
def inicio():
    return "Backend operante\n"

app.run(debug=True, host="0.0.0.0")