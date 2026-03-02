import random
import time  


class Base_cacador:
    def __init__(self, nome, vida, defesa, ataque, esquiva):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva

    def atacar(self, alvo):
        chance = random.randint(1, 100)
        if chance <= alvo.esquiva:
            print(f" {alvo.nome} desviou do ataque!")
        else:
            dano = self.ataque - alvo.defesa
            if dano < 0:
                dano = 0
            alvo.vida -= dano
            print(f" {self.nome} causou {dano} de dano em {alvo.nome}!")

    def status(self):
        print(f" {self.nome} | Vida: {self.vida}")

class AnjoDemoniaco(Base_cacador):
    def __init__(self, nome):
        super().__init__(nome, 150, 15, 22, 10)
        self.voando = False

    def voar(self):
        if not self.voando:
            self.voando = True
            self.esquiva += 20
            print(f" {self.nome} abriu as asas e voou! (Esquiva +20)")
        else:
            print(f" {self.nome} já está voando!")

class Base_monstro:
    def __init__(self, nome, vida, defesa, ataque, esquiva):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva

    def atacar(self, alvo):
        chance = random.randint(1, 100)
        if chance <= alvo.esquiva:
            print(f" {alvo.nome} desviou do ataque da {self.nome}!")
        else:
            dano = self.ataque - alvo.defesa
            if dano < 0:
                dano = 0
            alvo.vida -= dano
            print(f" {self.nome} causou {dano} de dano em {alvo.nome}!")

    def status(self):
        print(f" {self.nome} | Vida: {self.vida}")

class Sereia(Base_monstro):
    def __init__(self, nome):
        super().__init__(nome, 130, 18, 20, 12)
        self.mergulhada = False

    def mergulhar(self):
        if not self.mergulhada:
            self.mergulhada = True
            self.esquiva += 20
            print(f" {self.nome} mergulhou nas águas profundas! (Esquiva +20)")
        else:
            print(f" {self.nome} já está submersa!")

print("=" * 50)
print(" BATALHA: ANJO DEMONIACO vs SEREIA ")
print("=" * 50)


nome_cacador = input("\n Digite o nome do seu caçador (Anjo Demoniaco): ")
anjo = AnjoDemoniaco(nome_cacador)

nome_sereia = input(" Digite o nome da sua sereia: ")
sereia = Sereia(nome_sereia)


print("\n" + "-" * 40)
anjo.status()
anjo.voar()
anjo.status()

print("\n" + "-" * 40)
sereia.status()
sereia.mergulhar()
sereia.status()


print("\n" + "=" * 50)
print(" A BATALHA COMEÇOU! ")
print("=" * 50)

turno = 1
while anjo.vida > 0 and sereia.vida > 0:
    print(f"\n TURNO {turno}")
    print("-" * 20)

   
    if turno % 2 == 1: 
        anjo.atacar(sereia)
    else:              
        sereia.atacar(anjo)

   
    anjo.status()
    sereia.status()

    input("\n⏸  Pressione Enter para o próximo turno...")
    turno += 1


print("\n" + "=" * 50)
print(" FIM DA BATALHA ")
print("=" * 50)

if anjo.vida <= 0 and sereia.vida <= 0:
    print(" Empate! Ambos morreram ao mesmo tempo.")
elif anjo.vida <= 0:
    print(f" {anjo.nome} morreu... {sereia.nome} venceu! ")
else:
    print(f" {sereia.nome} morreu... {anjo.nome} venceu! ")

input("\nPressione Enter para sair.")