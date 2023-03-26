#classe dos seres vivos (PAI)
class Seres_vivos:
    def __init__(self):
        #ataque e vida do personagem(padrão)
        self.HP = 1000
        self.ataque = 100

    def atacar(self):
        return self.ataque

    def receber_ataque(self, saude, ataque):
        self.HP = saude - ataque
        return self.HP 
