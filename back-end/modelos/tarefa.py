from geral.config import *
from modelos.lista_tarefa import *

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text, nullable=False)
    concluido = db.Column(db.Boolean, default=False)
    lista_tarefa_id = db.Column(db.Integer, db.ForeignKey(ListaTarefa.id), nullable=False)

    def __str__(self) -> str:
        return f"ID: {self.id} ID da Lista de Tarefa: {self.lista_tarefa_id}, Conteúdo: {self.conteudo}, Conclúido: {self.concluido and '☑' or '☐'}"

    def json(self) -> dict:
        return {
            "id": self.id,
            "conteudo": self.conteudo,
            "concluido": self.concluido,
            "lista_tarefa_id": self.lista_tarefa_id,
        }