# 📘 Assignment: Creating Good Skills with Copilot

## 🎯 Objective

Aprenda a transformar conhecimento de domínio em uma skill clara e reutilizável para o GitHub Copilot, com escopo explícito, instruções acionáveis e critérios para verificar se o resultado está correto.

## 📝 Tasks

### 🛠️ Definir o propósito da skill

#### Descrição

Escolha um domínio que você conhece e escreva a especificação inicial de uma skill. Comece identificando quem usará a skill, qual problema ela resolve e em quais situações ela deve ser ativada.

#### Requisitos

A especificação concluída deve:

- Descrever um objetivo observável para a skill
- Identificar o público e o contexto de uso
- Listar pelo menos três situações em que a skill deve ser usada
- Delimitar pelo menos duas situações em que a skill não deve ser usada

### 🛠️ Escrever instruções úteis

#### Descrição

Crie um arquivo `SKILL.md` com frontmatter válido e instruções que guiem o Copilot por um fluxo reproduzível. Organize o conteúdo para que uma pessoa nova consiga seguir as etapas sem depender de conhecimento implícito.

#### Requisitos

A skill concluída deve:

- Conter `name` e `description` no frontmatter
- Explicar claramente quando usar e quando não usar a skill
- Apresentar etapas ordenadas, entradas esperadas e formato da saída
- Usar exemplos curtos e concretos quando eles reduzirem ambiguidades
- Evitar instruções vagas, contraditórias ou que repitam regras sem necessidade

### 🛠️ Testar e melhorar a skill

#### Descrição

Faça pelo menos três testes com pedidos representativos, incluindo um pedido fora do escopo. Compare as respostas com os critérios definidos e revise a skill para corrigir ambiguidades ou resultados inconsistentes.

#### Requisitos

A avaliação concluída deve:

- Registrar três cenários de teste e o resultado esperado de cada um
- Incluir pelo menos um caso-limite ou pedido fora do escopo
- Verificar se a skill produz respostas consistentes com seu objetivo
- Documentar pelo menos uma melhoria feita após os testes
- Explicar como outra pessoa pode repetir a validação
