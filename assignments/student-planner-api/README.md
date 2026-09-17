# 📘 Atividade: Student Planner API

## 🎯 Objetivo

Construir uma API REST para organizar tarefas de estudo de um aluno, usando FastAPI para criar endpoints, validar entrada e devolver respostas claras em JSON.

## 📝 Tarefas

### 🛠️ Configurar a aplicação

#### Descrição

Use o arquivo inicial para criar a estrutura básica de uma API FastAPI e preparar um armazenamento simples em memória para tarefas.

#### Requisitos
A aplicação concluída deve:

- Criar uma instância de `FastAPI`
- Definir um modelo de tarefa com pelo menos `id`, `title`, `subject`, `priority` e `completed`
- Iniciar com uma lista pequena de tarefas de exemplo
- Disponibilizar `GET /tasks` para listar todas as tarefas
- Permitir que a aplicação seja executada com `uvicorn`

### 🛠️ Implementar CRUD

#### Descrição

Adicione endpoints para criar, consultar, atualizar e remover tarefas do planner.

#### Requisitos
A aplicação concluída deve:

- Disponibilizar `POST /tasks` para criar uma nova tarefa
- Disponibilizar `GET /tasks/{task_id}` para buscar uma tarefa por ID
- Disponibilizar `PATCH /tasks/{task_id}` para atualizar campos da tarefa
- Disponibilizar `DELETE /tasks/{task_id}` para remover uma tarefa
- Retornar status `404` quando uma tarefa não existir
- Responder com `201` ao criar uma nova tarefa

### 🛠️ Validar dados e filtrar resultados

#### Descrição

Melhore a API adicionando validação para entradas inválidas e filtros para buscar tarefas por status e disciplina.

#### Requisitos
A aplicação concluída deve:

- Validar que `title` e `subject` não estejam vazios
- Validar que `priority` esteja entre `1` e `5`
- Permitir filtros por `status` e `subject` em `GET /tasks`
- Retornar uma resposta adequada para entradas inválidas
- Usar modelos de resposta e tipos claros para facilitar a documentação automática em `/docs`
