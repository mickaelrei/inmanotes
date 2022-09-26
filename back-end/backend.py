from geral.config import *
from rotas.listar import *

@app.route("/")
def inicio():
    return "Backend operante\n"

app.run(debug=True)