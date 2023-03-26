from Seres_Vivos import Seres_vivos

#Classe do personagem
class Personagem(Seres_vivos):
    def __init__(self, nome):
        self.nome = nome
        print(f"Seu nome é {self.nome}, Vamos para a batalha!")