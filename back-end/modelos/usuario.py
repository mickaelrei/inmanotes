from geral.config import *
from modelos.cargo import Cargo

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(254), nullable=False)
    nome_display = db.Column(db.String(254), nullable=False)
    data_criacao = db.Column(db.Date, nullable=False)
    foto = db.Column(db.Text, default="") # Endereço da imagem
    senha = db.Column(db.String(254), nullable=False)

    cargo_id = db.Column(db.Integer, db.ForeignKey(Cargo.id), nullable=False)
    cargo = db.relationship("Cargo")

    listas_tarefas = db.relationship("ListaTarefa", backref="usuario")
    notas = db.relationship("Nota", backref="usuario")

    def __str__(self) -> str:
        s = f"ID: {self.id} ID de cargo: {self.cargo_id}, Nome de usuário: {self.nome_usuario}, Nome de display: {self.nome_display}, Data de criação da conta: {self.data_criacao}, Caminho da foto: {self.foto}, Senha: {self.senha}. Notas:"

        for nota in self.notas:
            s += f"\n ・ {nota}"

        s += "\n\nListas de Tarefas:"

        for lista in self.listas_tarefas:
            s += f"\n ・ {lista}"

        return s

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