from geral.config import *
from modelos.nota import Nota
from modelos.tarefa import Tarefa
from modelos.lista_tarefa import ListaTarefa
from datetime import datetime
import os

if __name__ == "__main__":
    # Remover arquivo db
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Cria tabelas
    db.create_all()

    nota = Nota(nome="teste", titulo="Testando", conteudo="testando classe nota.\n\nApenas forte",
                data_criacao=datetime.now())
    db.session.add(nota)

    compras = [
        "Banana",
        "Leite",
        "Maçã",
        "Ovo",
        "Macarrão",
        "Aveia",
        "Whey"
    ]
    compras_obj = []
    lista_tarefa = ListaTarefa(titulo="Lista de compras")
    for compra in compras:
        tarefa = Tarefa(conteudo=compra, concluido=True, lista_tarefa=lista_tarefa)
        # compras_obj.append(tarefa)
        db.session.add(tarefa)

    db.session.add(lista_tarefa)
    db.session.commit()