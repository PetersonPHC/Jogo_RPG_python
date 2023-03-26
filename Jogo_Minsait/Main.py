'''Arquivo Principal, Jogo rodando'''

from Seres_Vivos import Seres_vivos
from Monstros import Monstro
from Personagem import Personagem

#Mensagem inicial do game
print("*"*40)
print("!!! O Jogo Começou !!!")
print("*"*40)

#Jogo Funcionando
NomePerson = input("Bem Vindo(a)\nInsira seu Nome: ")
NomePerson = Personagem(nome= NomePerson)
print("")
jogador = Seres_vivos()

print(f"Você esta caminhando e encontra um monstro...")

globin = Monstro(tipo="globin")#Luta contra Um Globin
while globin.HP > 0:
    print(f"Globin te atacou e causou {globin.atacar()} de dano!")
    jogador.receber_ataque(saude= jogador.HP ,ataque= globin.atacar())
    print(f"Você atacou o globin e causou {jogador.atacar()} de dano!")
    globin.receber_ataque (saude= globin.HP ,ataque= jogador.atacar())
    if (jogador.HP < 0):
        print("Game Over")
        break

print("\nPARABENS! Você derrotou o globin!")
print("Você continua sua Aventura, porém encontra outro terrível oponente...")

lobo = Monstro(tipo="lobo")#luta contra um Lobo
while lobo.HP > 0:
    print(f"Lobo te atacou e causou {lobo.atacar()} de dano!")
    jogador.receber_ataque(saude= jogador.HP ,ataque= lobo.atacar())
    print(f"Você atacou o Lobo e causou {jogador.atacar()} de dano!")
    lobo.receber_ataque (saude= lobo.HP ,ataque= jogador.atacar())
    if (jogador.HP < 0):
        print("Game Over")
        break

print("\nPARABENS! Você derrotou o terrível Lobo!\n")

print(f"Após esta longa aventura cheia de obstaculos e batalhas Você {NomePerson.nome} Venceu e foi Aprovado! ")