from flask import Flask, jsonify, request, session, render_template
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import os
import sys
from flask_cors import CORS, cross_origin
from datetime import timedelta

caminho_template = "../../front-end"
static_template = "../../front-end/static"
app = Flask(__name__, template_folder=caminho_template, static_folder=static_template)
app.app_context().push()
CORS(app)

# Caminho do arquivo do banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'inmanotes.db')

# Configurações
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config["JWT_SECRET_KEY"] = "secretKey"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
app.config["JWT_TOKEN_LOCATION"] = ["headers", "query_string"]
jwt = JWTManager(app)