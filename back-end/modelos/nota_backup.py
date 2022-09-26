# from geral.config import *
# from modelos.nota import *

# class ListaTarefa(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tarefas = db.relationship("Tarefa", backref="lista_tarefa")

#     def json(self) -> dict:
#         return {
#             "titulo": self.titulo,
#             "conteudo": self.conteudo,
#             "concluido": self.concluido
#         }