from geral.config import *
from modelos.cargo import Cargo

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(254))
    nome_display = db.Column(db.String(254))
    foto = db.Column(db.Text, default="") # Endereço da imagem
    senha = db.Column(db.String(254))

    cargo_id = db.Column(db.Integer, db.ForeignKey(Cargo.id), nullable=False)
    cargo = db.relationship("Cargo")

    listas_tarefas = db.relationship("ListaTarefa", backref="usuario")
    notas = db.relationship("Nota", backref="usuario")

    def json(self) -> dict:
        obj = {
            "id": self.id,
            'nome_usuario': self.nome_usuario,
            "nome_display": self.nome_display,
            "foto": self.foto,
            "senha": self.senha,
            "cargo": self.cargo.json(),
        }

        listas_tarefas = []
        for lista in self.listas_tarefas:
            listas_tarefas.append(lista.json())
        obj.update({"listas_tarefas": listas_tarefas})

        notas = []
        for nota in self.notas:
            notas.append(nota.json())

        obj.update({"notas": notas})
        return obj