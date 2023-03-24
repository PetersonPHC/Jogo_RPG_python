from Seres_Vivos import seres_vivos
class monstro(seres_vivos):
    def __init__(self, tipo):
        self.tipo = tipo
        match self.tipo:
            case "globin":
                print("Você encontru um globin!")
                self.HP = 200
                self.ataque = 20
                self.inteligencia = 150

            case "lobo":
                print("Você encontru um lobo")
                self.HP = 500
                self.ataque = 100
                self.forcaExtra = 50
                self.ataque = self.ataque + self.forcaExtra

class personagem(seres_vivos):
    def __init__(self, nome):
        self.nome = nome
        print(f"Seu nome é {self.nome}, Vamos para a batalha!")
        
#Jogo Funcionando
NomePerson = input("Bem Vindo(a)\nInsira seu Nome: ")
NomePerson = personagem(NomePerson)
jogador = seres_vivos()


print(f"Você esta caminhando e encontra um monstro")

globin = monstro("globin")
while globin.HP > 0:
    print(f"Globin te atacou e causou {globin.atacar()} de dano!")
    jogador.receber_ataque(jogador.HP , globin.atacar())
    print(f"Você atacou o globin e causou {jogador.atacar()} de dano!")
    globin.receber_ataque (globin.HP , jogador.atacar())
    if (jogador.HP < 0):
        print("Game Over")
        break

print("PARABENS! Você derrotou o globin!")

lobo = monstro("lobo")
while lobo.HP > 0:
    print(f"Lobo te atacou e causou {lobo.atacar()} de dano!")
    jogador.receber_ataque(jogador.HP , lobo.atacar())
    print(f"Você atacou o Lobo e causou {jogador.atacar()} de dano!")
    lobo.receber_ataque (lobo.HP , jogador.atacar())
    if (jogador.HP < 0):
        print("Game Over")
        break

print("PARABENS! Você derrotou o terrível Lobo!")

print(f"Após esta longa aventura cheia de obstaculos e batalhas Você {NomePerson.nome} Venceu e foi Aprovado! ")