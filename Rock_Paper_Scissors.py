# Jogo "Pedra Papel Tesoura" V:0.0 #
# Coder: Rafael Gusmão #

import random

# 01 Instanciar variáveis #
Escolha_Jogador = input("Escolhe um (pedra, papel, tesoura): ").lower()
pc = random.choice(("pedra", "papel", "tesoura"))

# 02 Lógica #
def escolha():
    if Escolha_Jogador == "pedra" and pc == "tesoura":
        return "Jogador Ganhou"
    if Escolha_Jogador == "pedra" and pc == "papel":
        return "Jogador Perdeu"
    if Escolha_Jogador == "pedra" and pc == "pedra":
        return "Jogador Empatou"
    if Escolha_Jogador == "papel" and pc == "pedra":
        return "Jogador Ganhou"
    if Escolha_Jogador == "papel" and pc == "papel":
        return "Jogador Empatou"
    if Escolha_Jogador == "papel" and pc == "tesoura":
        return "Jogador Perdeu"
    if Escolha_Jogador == "tesoura" and pc == "pedra":
        return "Jogador Perdeu"
    if Escolha_Jogador == "tesoura" and pc == "papel":
        return "Jogador Ganhou"
    if Escolha_Jogador == "tesoura" and pc == "tesoura":
        return "Jogador Empatou"
    return ""

resultado = escolha()

while True:
    if resultado != "":
        break
    print("Escolha Errada")
    Escolha_Jogador = input("Escolhe um (pedra, papel, tesoura): ").lower()
    resultado = escolha()

# 03 Resultado #
print(resultado)
print("Jogador:", Escolha_Jogador, "| PC:", pc)
