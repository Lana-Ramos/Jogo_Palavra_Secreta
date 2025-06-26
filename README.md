# 🎯 Jogo da Palavra Secreta – Python

## 📄 Descrição

Este projeto implementa um jogo de adivinhação de palavras em Python, no qual o usuário deve descobrir qual é a palavra secreta digitando **uma letra por vez**.

O jogo permite que uma pessoa digite uma palavra e outra tente adivinhar, recebendo dicas conforme acerta letras. O código também valida a entrada do usuário, impede letras repetidas e mostra as letras já tentadas.


## 🛠️ Funcionalidades

* ✅ Definição da palavra secreta por um jogador
* ✅ Exibição progressiva da palavra com `*` para letras não descobertas
* ✅ Entrada de **uma letra por vez**, validada (alfabética, única e não repetida)
* ✅ Mensagens claras e interativas para o usuário
* ✅ Contagem de tentativas do jogador
* ✅ Exibição das letras já chutadas
* ✅ Possibilidade de jogar quantas vezes quiser


## 💻 Tecnologias Utilizadas

* Linguagem: **Python 3**
* Terminal padrão (não requer bibliotecas externas)
* Compatível com **Windows**, **Linux** e **macOS**


## ▶️ Como Executar

1. Instale o Python 3: [Download Python](https://www.python.org/downloads/)
2. Clone este repositório ou copie o código.
3. Salve o arquivo como `Jogo_Palavra_Secreta.py`.
4. Execute no terminal com o comando:

```bash
python Jogo_Palavra_Secreta.py
```


## 📸 Demonstração

```text
A palavra secreta é: p * * t * *
Letras que já foram chutadas: (['p', 't'])
Chute uma letra:
```


## 🔄 Reinício do Jogo

Após adivinhar corretamente a palavra, o programa pergunta:

```
Deseja jogar novamente? [Sim/Não]
```

Basta responder para reiniciar com uma nova palavra secreta.


## 🧠 Conceitos Aplicados

* Laços `while` e `for`
* Listas (`append`, `in`, `join`)
* Condicionais `if`, `continue`
* Funções de string (`lower()`, `isalpha()`)
* Limpeza de tela com `os.system("cls")` ou `"clear"`
* Controle de fluxo e validação de dados do usuário


## 👩‍💻 Autora

**Lana Ramos Gomes**

## 📘 Licença

MIT - Este projeto é livre para uso educacional e aprendizado.
