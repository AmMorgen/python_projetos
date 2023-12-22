alfabeto = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'q','r','s'
            ,'t','u','v','w','y','z', 'a', 'b', 'c', 'd','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'q','r','s'
            ,'t','u','v','w','y','z']

direcao = input("Digite 'codificar' para criptografar e 'decodificar' para descriptografar\n")
texto = input("Digite sua mensagem:\n").lower()
deslocamento = int(input("Digite o deslocamento\n"))

def criptografar(textol, deslocamento2):
    cifra_texto = ""
    for letter in textol:
        posicao = alfabeto.index(letter)
        nova_posicao = posicao + deslocamento2
        nova_letra = alfabeto[nova_posicao]
        cifra_texto += nova_letra
    print(f"O texto criptografado é {cifra_texto} ")


def descriptografar(texto_cifra, deslocamento3):
    plain_text = ""
    for letter in texto_cifra:
        posicao = alfabeto.index(letter)
        nova_posicao = posicao - deslocamento3
        plain_text += alfabeto[nova_posicao]
    print(f"O texto criptografado é {plain_text} ")




if direcao == "codificar": 
    criptografar(textol=texto,deslocamento2=deslocamento)
elif direcao == "decodificar":
    descriptografar(texto_cifra=texto,deslocamento3=deslocamento)
else:
    print("erro")