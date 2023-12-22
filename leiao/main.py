import os


def ache_maior_oferta(registro_ofertas):
    maior_oferta = 0
    for ofertas in registro_ofertas:
        total_ofertas = registro_ofertas[ofertas]
        if total_ofertas > maior_oferta:
            maior_oferta = total_ofertas
            ganhador = ofertas
        print(f"O vencedor é {ganhador} com a oferta de {maior_oferta}")
ofertas_acabaram = False



while not ofertas_acabaram:
    ofertas = {}
    nome = input("Diga seu nome\n")
    preco = int(input("Qual a sua oferta? R$ "))
    ofertas[nome] = preco
    continuar = input("Há akguma outra oferta? Dgite 'Sim' ou 'Não' ").lower()
    if continuar == 'não':
        ofertas_acabaram = True
        ache_maior_oferta(ofertas)
    elif continuar == 'sim':
        os.system("cls")