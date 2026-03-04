import random

class Entidade:
    def _init_(self, nome, vida, defesa, ataque, esquiva):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque
        self.esquiva = esquiva

    def atacar(self, alvo):
        chance = random.randint(1, 100)

        if chance <= alvo.esquiva:
            print(f" {alvo.nome} desviou!")
        else:
            dano = self.ataque - alvo.defesa
            if dano < 0:
                dano = 0
            alvo.vida -= dano
            print(f" {self.nome} causou {dano} de dano em {alvo.nome}!")

    def status(self):
        print(f"{self.nome} | Vida: {self.vida}")