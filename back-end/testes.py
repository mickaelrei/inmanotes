import sys
# Desativar criação das pastas __pycache__
sys.dont_write_bytecode = True
from geral.config import *
from geral.cripto import *
from modelos.nota import Nota
from modelos.tarefa import Tarefa
from modelos.lista_tarefa import ListaTarefa
from modelos.usuario import Usuario
from modelos.cargo import Cargo
from datetime import datetime
import os
from random import random

if __name__ == "__main__":
    # Remover arquivo db
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Cria tabelas
    db.create_all()

    # Cargos
    cargo_usuario = Cargo(nome="usuario", descricao="Usuário comum, com permissão para criar, editar e excluir suas próprias notas e listas de tarefa")
    cargo_administrador = Cargo(nome="administrador", descricao="Administrador, com permissão de usuário comum além de poder acessar e excluir notas e listas de tarefa de outros usuários")
    db.session.add(cargo_usuario)
    db.session.add(cargo_administrador)

    # Usuario 1
    senha = cifrar("123senhaforte123")
    usuario1 = Usuario(nome="Mickael", email="mickael.reichert@gmail.com", senha=senha, cargo=cargo_administrador, data_criacao=datetime.now())
    db.session.add(usuario1)
    
    # Nota
    nota = Nota(nome="teste", titulo="Testando", conteudo="testando classe nota. Texto base",
                data_criacao=datetime.now(), usuario=usuario1)
    db.session.add(nota)

    # Lista 1: compras
    compras = [
        "Banana",
        "Leite",
        "Maçã",
        "Ovo",
        "Macarrão",
        "Aveia",
        "Whey"
    ]
    lista_tarefa_compras = ListaTarefa(titulo="Lista de compras", usuario=usuario1, data_criacao=datetime.now())
    db.session.add(lista_tarefa_compras)

    for compra in compras:
        tarefa = Tarefa(conteudo=compra, lista_tarefa=lista_tarefa_compras, concluido=random() > .5)
        db.session.add(tarefa)

    # Lista 2: atividades
    lista_tarefa_atividades = ListaTarefa(titulo="Lista de Atividades", usuario=usuario1, data_criacao=datetime.now())
    db.session.add(lista_tarefa_atividades)

    atividades = [
        "Trabalho Evolução",
        "Exercícios Matemática",
        "Pesquisar sobre vagas de emprego"
    ]
    for atv in atividades:
        tarefa = Tarefa(conteudo=atv, lista_tarefa=lista_tarefa_atividades, concluido=random() > .5)
        db.session.add(tarefa)

    db.session.commit()

    # Printa os objetos criados
    print(f"\n{usuario1}\n")
    print(nota, "\n")
    print(lista_tarefa_compras,"\n")
    print(lista_tarefa_atividades,"\n")