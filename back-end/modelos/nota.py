from geral.config import *
from modelos.usuario import *

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, nullable=False)
    titulo = db.Column(db.String(254), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)

    def __str__(self) -> str:
        return f"ID: {self.id} ID do usuário: {self.usuario_id}, Data de criação: {self.data_criacao}, Título: {self.titulo}, Conteúdo: {self.conteudo}"

    def json(self) -> dict:
        return {
            "id": self.id,
            "data_criacao": self.data_criacao,
            "titulo": self.titulo,
            "conteudo": self.conteudo,
            "usuario_id": self.usuario_id
        }