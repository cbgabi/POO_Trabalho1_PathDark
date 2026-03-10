from jogador import AnjoDemoniaco
from inimigo import Sereia


def batalha(jogador, inimigo):
    while jogador.esta_vivo() and inimigo.esta_vivo():

        print(jogador.status())
        print(inimigo.status())

        escolha = jogador.escolher_acao()

        if escolha == "1":
            print(jogador.atacar(inimigo))
        elif escolha == "2":
            print(jogador.habilidade_especial())

        if inimigo.esta_vivo():
            print(inimigo.atacar(jogador))

        print()

    if jogador.esta_vivo():
        print("🏆 Jogador venceu!")
    else:
        print("💀 Inimigo venceu!")


if __name__ == "__main__":
    anjo = AnjoDemoniaco("Malak")
    sereia = Sereia("Sadna")

    batalha(anjo, sereia)