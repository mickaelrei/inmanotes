from geral.config import *

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.Date)
    nome = db.Column(db.String(254), nullable=False)
    titulo = db.Column(db.String(254), nullable=False)
    conteudo = db.Column(db.Text)

    def json(self) -> dict:
        return {
            "data_criacao": self.data_criacao,
            "nome": self.nome,
            "titulo": self.titulo,
            "conteudo": self.conteudo
        }