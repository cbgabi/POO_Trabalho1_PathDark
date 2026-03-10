from entidade import Entidade

class Jogador(Entidade):

    def __init__(self, nome, vocacao):
        super().__init__(
            nome,
            100 + vocacao.bonus_vida,
            10 + vocacao.bonus_defesa,
            10 + vocacao.bonus_ataque,
            5 + vocacao.bonus_esquiva
        )

        self.vocacao = vocacao
        self.exp = 0
        self.nivel = 1

    def mostrar_vocacao(self):
        print(f"Vocação: {self.vocacao.nome}")

    def ganhar_exp(self, quantidade):
        print(f"\n Você ganhou {quantidade} EXP!")
        self.exp += quantidade

        if self.exp >= 100:
            self.nivel += 1
            self.exp = 0
            self.vida += 20
            self.ataque += 5
            self.defesa += 3

            print(" LEVEL UP!")
            print(f"Você agora é nível {self.nivel}")
