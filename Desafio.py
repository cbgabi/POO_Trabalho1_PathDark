import random

def bau_raro(jogador):
    print("\n Você encontrou um BAÚ RARO!")

    evento = random.choice([
        "super_cura",
        "buff_ataque",
        "buff_defesa",
        "exp_bonus",
        "armadilha_forte",
        "jackpot"
    ])

    if evento == "super_cura":
        cura = random.randint(30, 60)
        jogador.vida += cura
        print(f" Poção lendária! +{cura} de vida!")

    elif evento == "buff_ataque":
        jogador.ataque += 10
        print(" Seu ataque aumentou MUITO! (+10)")

    elif evento == "buff_defesa":
        jogador.defesa += 8
        print(" Sua defesa aumentou! (+8)")

    elif evento == "exp_bonus":
        exp = random.randint(40, 80)
        jogador.ganhar_exp(exp)

    elif evento == "armadilha_forte":
        dano = random.randint(20, 40)
        jogador.vida -= dano
        print(f" Armadilha poderosa! Você perdeu {dano} de vida!")

    elif evento == "jackpot":
        jogador.vida += 50
        jogador.ataque += 5
        jogador.defesa += 5
        print(" JACKPOT! Vida +50 | Ataque +5 | Defesa +5")
