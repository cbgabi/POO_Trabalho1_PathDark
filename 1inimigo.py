from entidade import Entidade


class Bruxa(Entidade):
    def __init__(self):
        super().__init__("Bruxa", 40, 3, 6, 5)
        self.exp_recompensa = 20


class Ghoul(Entidade):
    def __init__(self):
        super().__init__("Ghoul", 45, 4, 7, 4)
        self.exp_recompensa = 25


class Grifo(Entidade):
    def __init__(self):
        super().__init__("Grifo", 50, 3, 8, 8)
        self.exp_recompensa = 30


class AranhaGigante(Entidade):
    def __init__(self):
        super().__init__("Aranha Gigante", 35, 2, 5, 2)
        self.exp_recompensa = 20


class Morcego(Entidade):
    def __init__(self):
        super().__init__("Morcego", 30, 2, 6, 10)
        self.exp_recompensa = 20


class SereiaAbisal(Entidade):
    def __init__(self):
        super().__init__("Sereia Abisal", 80, 10, 15, 6)
        self.exp_recompensa = 45


class Lobisomem(Entidade):
    def __init__(self):
        super().__init__("Lobisomem", 75, 9, 14, 12)
        self.exp_recompensa = 50


class Vampiro(Entidade):
    def __init__(self):
        super().__init__("Vampiro", 85, 8, 16, 14)
        self.exp_recompensa = 55


class Troll(Entidade):
    def __init__(self):
        super().__init__("Troll", 70, 7, 13, 10)
        self.exp_recompensa = 50


class Fantasma(Entidade):
    def __init__(self):
        super().__init__("Fantasma", 65, 6, 12, 15)
        self.exp_recompensa = 45


class Doppelganger(Entidade):
    def __init__(self):
        super().__init__("Doppelganger", 120, 15, 22, 18)
        self.exp_recompensa = 80


class Demonio(Entidade):
    def __init__(self):
        super().__init__("Demônio", 140, 18, 25, 12)
        self.exp_recompensa = 90


class Dragao(Entidade):
    def __init__(self):
        super().__init__("Dragão", 160, 20, 28, 10)
        self.exp_recompensa = 100


class Necromante(Entidade):
    def __init__(self):
        super().__init__("Necromante", 110, 14, 21, 16)
        self.exp_recompensa = 85


class Hidra(Entidade):
    def __init__(self):
        super().__init__("Hidra", 170, 22, 30, 8)
        self.exp_recompensa = 120

inimigos = {

    "fracos": [
        Base_monstro("bruxa", vida=40, defesa=3, ataque=6, esquiva=5),
        Base_monstro("ghoul", vida=45, defesa=4, ataque=7, esquiva=4),
        Base_monstro("grifo", vida=50, defesa=3, ataque=8, esquiva=8),
        Base_monstro("aranha gigante", vida=35, defesa=2, ataque=5, esquiva=2),
        Base_monstro("Morcego", vida=30, defesa=2, ataque=6, esquiva=10)
    ],

    "medios": [
        Base_monstro("sereia abisal", vida=80, defesa=10, ataque=15, esquiva=6),
        Base_monstro("Lobisomem", vida=75, defesa=9, ataque=14, esquiva=12),
        Base_monstro("Vampiro", vida=85, defesa=8, ataque=16, esquiva=14),
        Base_monstro("troll", vida=70, defesa=7, ataque=13, esquiva=10),
        Base_monstro("Fantasma", vida=65, defesa=6, ataque=12, esquiva=15)
    ],

    "fortes": [
        Base_monstro("Doppelganger ", vida=120, defesa=15, ataque=22, esquiva=18),
        Base_monstro("Demônio", vida=140, defesa=18, ataque=25, esquiva=12),
        Base_monstro("Dragão", vida=160, defesa=20, ataque=28, esquiva=10),
        Base_monstro("Necromante", vida=110, defesa=14, ataque=21, esquiva=16),
        Base_monstro("Hidra", vida=170, defesa=22, ataque=30, esquiva=8)
    ]
}
