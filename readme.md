# Inmanotes

Este projeto consiste em um aplicativo de criação e edição de notas e lista de tarefas.

## Documentação de rotas

Comandos para acessar rotas do backend

### Registrar uma conta

    curl localhost:5000/registrar -H "Content-Type:application/json" -X POST -d "{\"nome\": \"seu nome\", \"email\": \"seu email\", \"foto\": \"caminho da sua foto\", \"senha\": \"sua senha\"}"

Resposta:

    {
        "detalhes": "ok", 
        "resultado": "ok"
    }


### Realizar login em uma conta

    curl localhost:5000/login -H "Content-Type:application/json" -X POST -d "{\"email\": \"seu email\", \"senha\": \"sua senha\"}"

Resposta:

    {
        "detalhes": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg", 
        "resultado": "ok"
    }

O código devolvido no campo "detalhes" é o JWT que será usado para acessar outras rotas.

### Registrar uma nota no seu usuário

Primeiro encontre o seu ID de usuário:

    curl localhost:5000/listar/usuario -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg"

Resposta:

    {
        "detalhes": [
            {
            "cargo": {
                "descricao": "Adminstrador, com permiss\u00e3o de usu\u00e1rio comum al\u00e9m de poder acessar e excluir notas e listas de tarefa de outros usu\u00e1rios", 
                "id": 2, 
                "nome": "administrador"
            }, 
            "email": "mickael.reichert@gmail.com", 
            "foto": "", 
            "id": 1, 
            "listas_tarefas": [
                {
                "data_criacao": "Wed, 09 Nov 2022 23:34:41 GMT", 
                "id": 1, 
                "tarefas": [
                    {
            
    ...

                {
            "cargo": {
                "descricao": "Usu\u00e1rio comum, com permiss\u00e3o para criar, editar e excluir suas pr\u00f3prias notas e listas de tarefa", 
                "id": 1, 
                "nome": "usuario"
            }, 
            "email": "emailteste@gmail.com", 
            "foto": "sem_foto", 
            "id":   3, 
            "listas_tarefas": [],
            "nome": "gabriel teste",
            "notas": [], 
            "senha": "gAAAAABjbOH5vCEaFsZytkXeH1Weus7pcunIZj0Es_4sTpgsVB-hp5bXDP9R5ZdgLtg8jzyPHw13xzRvhvESP9tiNObRLFBIGw=="
            }
        ], 
        "resultado": "ok"
    }

Utilizando o JWT e o ID de usuário (nesse caso 3), crie uma nota:

    curl localhost:5000/inserir/nota -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg" -d "{\"nome\": \"nome nota teste\", \"titulo\": \"titulo nota teste\", \"conteudo\": \"testando rota inserir\", \"usuario_id\": 3}"

### Listar as notas

    curl localhost:5000/listar/nota -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg"