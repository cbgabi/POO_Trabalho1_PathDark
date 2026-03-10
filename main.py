import random

from jogador import Jogador
from vocacao import Vocacao
from inimigo import inimigos


print(" RPG BATALHA ")

print("Escolha a dificuldade")
print("1 - facil")
print("2 - Médio")
print("3 - dificil")

opcao = int(input("Opção: "))

if opcao == 1:
    classe_inimigo = random.choice(inimigos["fracos"])

elif opcao == 2:
    classe_inimigo = random.choice(inimigos["medios"])

else:
    classe_inimigo = random.choice(inimigos["fortes"])

inimigo = classe_inimigo()


guerreiro = Vocacao("Guerreiro", 30, 10, 5, 2)

nome = input("Nome do jogador: ")

jogador = Jogador(nome, guerreiro)

print(f"\n Um {inimigo.nome} apareceu!")

turno = 1

while jogador.vida > 0 and inimigo.vida > 0:

    print(f"\nTurno {turno}")

    if turno % 2 == 1:
        jogador.atacar(inimigo)
    else:
        inimigo.atacar(jogador)

    jogador.status()
    inimigo.status()

    input("Pressione Enter...")
    turno += 1


print("\nFim da batalha!")

if jogador.vida > 0:
    print("Você venceu!")
    jogador.ganhar_exp(inimigo.exp_recompensa)
else:
    print("Você perdeu!")
