from Seres_Vivos import Seres_vivos

#Classe dos monstros (Filha)
class Monstro(Seres_vivos):
    def __init__(self, tipo):
        self.tipo = tipo
        match self.tipo:
            case "globin":
                print("VOCÊ ENCONTROU UM GLOBIN!\n")
                self.HP = 200
                self.ataque = 20
                self.inteligencia = 150

            case "lobo":
                print("VOCÊ ENCONTROU UM LOBO!\n")
                self.HP = 500
                self.ataque = 100
                self.forcaExtra = 50
                self.ataque = self.ataque + self.forcaExtra

        