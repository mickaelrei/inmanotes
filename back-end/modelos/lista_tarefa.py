from geral.config import *
from modelos.tarefa import *

class ListaTarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    tarefas = db.relationship("Tarefa", backref="lista_tarefa")

    def json(self) -> dict:
        return {
            "titulo": self.titulo,
            "tarefas": self.tarefas
        }