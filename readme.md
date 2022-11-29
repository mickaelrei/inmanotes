# Inmanotes

Este projeto consiste em um aplicativo de criação e edição de notas e lista de tarefas.

## Documentação de rotas

Comandos para acessar rotas do backend

## Registrar uma conta

    curl localhost:5000/registrarBack -H "Content-Type:application/json" -X POST -d "{\"nome\": \"seu nome\", \"email\": \"seu email\", \"foto\": \"caminho_foto\", \"senha\": \"sua senha\"}"

Resposta:

    {
        "detalhes": "ok", 
        "resultado": "ok"
    }

___

## Realizar login em uma conta

    curl localhost:5000/loginBack -H "Content-Type:application/json" -X POST -d "{\"email\": \"seu email\", \"senha\": \"sua senha\"}"

Resposta:

    {
        "detalhes": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg", 
        "resultado": "ok"
    }

O código devolvido no campo "detalhes" é o JWT que será usado para acessar outras rotas.

___

## Registrar uma nota no seu usuário

Utilizando seu JWT, crie uma nota informando os campos necessários no JSON:

    curl localhost:5000/inserir/nota -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg" -d "{\"nome\": \"nome nota teste\", \"titulo\": \"titulo nota teste\", \"conteudo\": \"testando rota inserir\"}"

___

## Listar suas notas

    curl localhost:5000/listar/nota -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODA4MDI0NCwianRpIjoiMjJlNmVmZDgtYTU5OC00YmRhLTg3OTQtODA5N2IwMmEzMDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVtYWlsdGVzdGVAZ21haWwuY29tIiwibmJmIjoxNjY4MDgwMjQ0LCJleHAiOjE2NjgwODA4NDR9.4DArfE89k-pw5NMydn1HvV6eHVo14oXjaiQvuo777jg"

___

## Testando backends de projetos de colegas

![Testando backends](testando_backends.png)