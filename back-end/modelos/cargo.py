from geral.config import *

class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.String(254), nullable=False)

    def __str__(self) -> str:
        return f"ID: {self.id}, Nome: {self.nome}, descrição: {self.descricao}"

    def json(self) -> dict:
       return {
        "id": self.id,
        "nome": self.nome,
        "descricao": self.descricao
       }