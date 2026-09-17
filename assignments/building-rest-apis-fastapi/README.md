# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, organizar endpoints, validar dados com modelos Pydantic e documentar o comportamento da API por meio de respostas HTTP claras.

## 📝 Tasks

### 🛠️ Criar o primeiro endpoint

#### Descrição

Use o arquivo inicial para executar uma aplicação FastAPI e crie um endpoint `GET /` que retorne uma mensagem informando que a API está funcionando.

#### Requisitos

A aplicação concluída deve:

- Criar uma instância de `FastAPI`
- Disponibilizar `GET /` com status `200`
- Retornar um objeto JSON com a chave `message`
- Poder ser executada com `uvicorn`

### 🛠️ Adicionar recursos e parâmetros

#### Descrição

Transforme a aplicação em uma API de tarefas. Adicione endpoints para listar tarefas e buscar uma tarefa específica por seu identificador.

#### Requisitos

A aplicação concluída deve:

- Disponibilizar `GET /tasks` para retornar uma lista de tarefas
- Disponibilizar `GET /tasks/{task_id}` para retornar uma tarefa pelo ID
- Retornar status `404` quando o ID não existir
- Usar anotações de tipo nos parâmetros e nas respostas sempre que apropriado

### 🛠️ Validar dados com Pydantic

#### Descrição

Adicione um modelo Pydantic para criar novas tarefas e implemente `POST /tasks`. Teste também os casos em que os dados enviados não atendem às regras definidas.

#### Requisitos

A aplicação concluída deve:

- Definir um modelo de entrada com campos como `title` e `completed`
- Validar que o título seja obrigatório e não vazio
- Criar uma tarefa com `POST /tasks` e retornar status `201`
- Retornar uma resposta de validação apropriada para dados inválidos
- Demonstrar os endpoints na documentação automática em `/docs`
