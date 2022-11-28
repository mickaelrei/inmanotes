import sys
# Desativar criação das pastas __pycache__
sys.dont_write_bytecode = True

from geral.config import *
from rotas import *

@app.route("/")
def inicio():
    return "Mickael e Cauã. IP: 191.52.7.72:5000<br>Backend operante. Link para repositório: <a href='https://github.com/mickaelrei/inmanotes' target='_blank'>link</a>\n"      

@app.route("/login")
def loginFront():
    return render_template("login.html")

@app.route("/registrar")
def registrarFront():
    return render_template("registrar.html")




app.run(debug=True, host="0.0.0.0")