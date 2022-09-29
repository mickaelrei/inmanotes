from geral.config import *
from modelos.tarefa import *
from modelos.usuario import *

class ListaTarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    tarefas = db.relationship("Tarefa", backref="lista_tarefa")

    usuario_id = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)

    def json(self) -> dict:
        obj = {
            "id": self.id,
            "titulo": self.titulo,
        }

        # Lista de tarefas
        tarefas = []
        for tarefa in self.tarefas:
            tarefas.append(tarefa.json())

        obj.update({"tarefas": tarefas})
        return obj