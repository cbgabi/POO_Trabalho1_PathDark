from entidade1 import Entidade

class Jogador(Entidade):
    def _init_(self, nome, vocacao):
        super()._init_(
            nome,
            100 + vocacao.bonus_vida,
            10 + vocacao.bonus_defesa,
            10 + vocacao.bonus_ataque,
            5 + vocacao.bonus_esquiva
        )
        self.vocacao = vocacao

    def mostrar_vocacao(self):
        print(f" Vocação: {self.vocacao.nome}")