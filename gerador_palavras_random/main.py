import random
#o programa é tentar adivinhar se uma letra está contida numa palavra aleatoria
lista_palavras = ['flamengo', 'minji', 'pham']
#uma das palavras seram escolhidas aleatoriamente
#após isso o usuario vai escolher uma letra e o programa vai informar se essa letra esta na palavra em que posição
palavra_escolhida = random.choice(lista_palavras)
fim_do_jogo = False
display = []
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
vidas = 6
print(palavra_escolhida)
for _ in range(len(palavra_escolhida)):
    display += "_"
print(display)

while not fim_do_jogo:
    palpite = input("adivinha a letra: ").lower()
    
    for position in range(len(palavra_escolhida)):
        letter = palavra_escolhida[position]
        if letter == palpite:
            display[position] = letter

    if palpite not in palavra_escolhida:
        vidas -= 1
        if vidas ==0:
            fim_do_jogo = True
    print(f"{' '.join(display)}")
    if "_" not in display:
        fim_do_jogo = True
        print("Ganhou")
    
    print(stages[vidas])