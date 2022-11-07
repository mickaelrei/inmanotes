from geral.config import *
from modelos.cargo import Cargo
from cryptography.fernet import Fernet

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(319), nullable=False)
    data_criacao = db.Column(db.Date, nullable=False)
    foto = db.Column(db.Text, default="") # Endereço da imagem
    chave = db.Column(db.String(254))
    senha_cripto = db.Column(db.String(254), nullable=False)

    @property
    def senha(self) -> None:
        raise AttributeError("Sem permissão para acessar a senha")

    @senha.setter
    def senha(self, _senha: str) -> None:
        print("Chave gerada")
        self.chave = Fernet.generate_key().decode()
        fernet = Fernet(self.chave.encode())
        self.senha_cripto = fernet.encrypt(_senha.encode())

    @senha.getter
    def senha(self) -> str:
        fernet = Fernet(self.chave.encode())
        return fernet.decrypt(self.senha_cripto).decode()

    cargo_id = db.Column(db.Integer, db.ForeignKey(Cargo.id), nullable=False)
    cargo = db.relationship("Cargo")

    listas_tarefas = db.relationship("ListaTarefa", backref="usuario")
    notas = db.relationship("Nota", backref="usuario")

    def __str__(self) -> str:
        s = f"ID: {self.id} ID de cargo: {self.cargo_id}, Nome: {self.nome}, E-Mail: {self.email}, Data de criação da conta: {self.data_criacao}, Caminho da foto: {self.foto}, Senha: {self.senha}. Notas:"

        for nota in self.notas:
            s += f"\n ・ {nota}"

        s += "\n\nListas de Tarefas:"

        for lista in self.listas_tarefas:
            s += f"\n ・ {lista}"

        return s

    def json(self) -> dict:
        obj = {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "foto": self.foto,
            "senha": self.senha_cripto.decode(),
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