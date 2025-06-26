import os
secret_word = ''
current_word = []
guesses=[]
trys = 0
answer = 's'
print("=====================================")
print("Bem vindo ao jogo da palavra secreta!")
print("=====================================")
print("Você vai precisar de duas pessoas:\n\n1-Uma digita a palavra secreta\n2-A outra tenta adivinhar")
print("=====================================")
input("Começando...\nPressione enter")

while answer.lower().startswith('s'):
    while True:
        os.system("cls")
        secret_word = input("Digite uma palavra para outra pessoa adivinhar: ").lower()

        #verificações se foi digitada uma palavra válida
        if len(secret_word)<=1:
            print("Digite uma palavra!")
            input("Pressione enter para continuar...")
            continue
        if not secret_word.isalpha(): #função que retorna true para todas as letras do alfabeto
            print("Digite apenas letras!")
            input("Pressione Enter para continuar...")
            continue
        break
    current_word = []
    guesses = []
    trys = 0
    for a in secret_word: # gera a palavra secreta com ****
        current_word.append('*')
    os.system("cls")
    while True:
        os.system("cls")
        if "*" not in current_word:
            print("PARABÉNS! Você acertou a palavra secreta!")
            print("Tentativas:", trys)
            break
        ''' Faz a mesma coisa que a função join: 
        mostra os itens da lista em seguida na mesma linha
        word='' 
        for i in current_word:
            word+=i
        '''
        print("A palavra secreta é:", "".join(current_word))
        print(f'Letras que já foram chutadas:({",".join(guesses)})')
        guessed_letter = input("Chute uma letra:").lower()

        #verificações se foi digitada uma letra válida
        if len(guessed_letter)>1:
            print("Digite apenas uma letra por vez!")
            input("Pressione enter para continuar...")
            continue
        if not guessed_letter.isalpha(): 
            print("Digite apenas letras!")
            input("Pressione Enter para continuar...")
            continue
        if guessed_letter in guesses:
            input("Você já chutou essa letra! Pressione Enter para continuar...")
            continue

        guesses.append(guessed_letter) # adicionando letra válida nas tentativas
        for index,letter in enumerate(secret_word):
            if letter==guessed_letter:
                current_word[index] = guessed_letter
        trys += 1
    answer = input("Deseja jogar novamente?[Sim/Não]")
os.system("cls")
print("=============================================")
print("Obrigada por jogar o jogo da palavra secreta!")
print("=============================================")