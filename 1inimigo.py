from entidade1 import Entidade

class Sereia(Entidade):
    def _init_(self, nome):
        super()._init_(nome, 130, 18, 20, 12)
        self.mergulhada = False

    def mergulhar(self):
        if not self.mergulhada:
            self.mergulhada = True
            self.esquiva += 20
            print(f" {self.nome} mergulhou! (Esquiva +20)")
        else:
            print(f" {self.nome} já está submersa!")