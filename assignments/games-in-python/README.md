
# 📘 Tarefa: Jogo da Forca

## 🎯 Objective

Pratique manipulação de strings, controle de fluxo e interação com o usuário ao criar um jogo da forca em Python.

## 📝 Tasks

### 🛠️ Escolher a Palavra Secreta

#### Descrição
Crie uma lista de palavras e escolha uma delas de forma aleatória para iniciar o jogo.

#### Requisitos
O programa completo deve:

- Definir uma lista com pelo menos 5 palavras possíveis.
- Selecionar uma palavra aleatória para o jogo.
- Armazenar a palavra escolhida de forma que possa ser comparada com as letras digitadas pelo jogador.

### 🛠️ Gerenciar as Tentativas do Jogador

#### Descrição
Permita que o usuário insira letras e acompanhe o progresso da palavra oculta durante o jogo.

#### Requisitos
O programa completo deve:

- Solicitar letras do usuário com `input()`.
- Mostrar o estado atual da palavra em formato como `_ _ _`.
- Verificar se a letra informada está presente na palavra secreta.
- Atualizar o progresso quando a letra for correta.
- Contar as tentativas incorretas restantes.

### 🛠️ Encerrar o Jogo com Resultado Final

#### Descrição
Finalize a partida quando o jogador acertar a palavra ou quando as tentativas acabarem.

#### Requisitos
O programa completo deve:

- Encerrar automaticamente quando a palavra for completamente revelada.
- Exibir uma mensagem de vitória quando o jogador adivinhar a palavra.
- Exibir uma mensagem de derrota quando as tentativas forem esgotadas.
- Mostrar a palavra correta ao final da partida.