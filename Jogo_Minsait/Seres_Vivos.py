class seres_vivos:
    def __init__(self):
        #ataque e vida do personagem
        self.HP = 1000
        self.ataque = 100

    def atacar(self):
        return self.ataque

    def receber_ataque(self, saude, ataque):
        self.HP = saude - ataque
        return self.HP 

print("*"*40)
print("!!! O Jogo Começou !!!")
print("*"*40)