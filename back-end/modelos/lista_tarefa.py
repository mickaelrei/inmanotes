from geral.config import *
from modelos.tarefa import *
from modelos.usuario import *

class ListaTarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254), nullable=False)
    tarefas = db.relationship("Tarefa", backref="lista_tarefa")
    data_criacao = db.Column(db.DateTime, nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)

    def __str__(self) -> str:
        s = f"ID: {self.id} ID do usuário: {self.usuario_id}, Título: {self.titulo}, Data de criação: {self.data_criacao}. Tarefas:"

        for tarefa in self.tarefas:
            s += f"\n - {tarefa}"

        return s

    def json(self) -> dict:
        obj = {
            "id": self.id,
            "titulo": self.titulo,
            "data_criacao": self.data_criacao,
            "usuario_id": self.usuario_id
        }

        # Lista de tarefas
        tarefas = []
        for tarefa in self.tarefas:
            tarefas.append(tarefa.json())

        obj.update({"tarefas": tarefas})
        return obj