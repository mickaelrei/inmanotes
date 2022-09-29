from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
import sys
sys.path.append('/home/aluno/inmanotes/back-end/geral')

from flask_cors import CORS, cross_origin  # permitir back receber json do front

# configurações
app = Flask(__name__)
CORS(app)  

# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'inmanotes.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remover warnings
db = SQLAlchemy(app)

# https://flask-session.readthedocs.io/en/latest/
# https://github.com/fengsp/flask-session/blob/master/test_session.py#L69
# app.secret_key = '$#EWFGHJUI*&DEGBHYJU&Y%T#RYJHG%##RU&U'
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
Session(app)