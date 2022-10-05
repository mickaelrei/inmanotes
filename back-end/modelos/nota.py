from geral.config import *
from modelos.usuario import *

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, nullable=False)
    nome = db.Column(db.String(254), nullable=False)
    titulo = db.Column(db.String(254), nullable=False)
    conteudo = db.Column(db.Text)

    usuario_id = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)

    def __str__(self) -> str:
        return f"ID: {self.id} ID do usuário: {self.usuario_id}, Data de criação: {self.data_criacao}, Nome: {self.nome}, Título: {self.titulo}, Conteúdo: {self.conteudo}"

    def json(self) -> dict:
        return {
            "id": self.id,
            "data_criacao": self.data_criacao,
            "nome": self.nome,
            "titulo": self.titulo,
            "conteudo": self.conteudo
        }