# Jogo "Pedra Papel Tesoura" V:0.0 #
# Coder: Rafael Gusmão #

import random

# 01 Instanciar variáveis #
Escolha_Jogador = input("Escolhe um (pedra, papel, tesoura): ")
pc = random.choice (("pedra", "papel", "tesoura"))

# 02 Lógica #


if Escolha_Jogador  == "pedra" and pc == "tesoura":
    resultado = "Jogador Ganhou"

if Escolha_Jogador == "pedra" and pc == "papel":
    resultado = "Jogador Perdeu"

if Escolha_Jogador == "pedra" and pc == "pedra":
    resultado = "Jogador Empatou"

if Escolha_Jogador == "papel" and pc == "pedra":
    resultado = "Jogador Perdeu"

if Escolha_Jogador == "papel" and pc == "papel":
    resultado = "Jogador Empatou"

if Escolha_Jogador == "papel" and pc == "tesoura":
    resultado = "Jogador Ganhou"

if Escolha_Jogador == "tesoura" and pc == "pedra":
    resultado = "Jogador Perdeu"

if Escolha_Jogador == "tesoura" and pc == "papel":
    resultado = "Jogador Ganhou"

if Escolha_Jogador == "tesoura" and pc == "tesoura":
    resultado = "Jogador Empatou"

# 03 Resultado #
print(resultado)
print("Jogador:", Escolha_Jogador, "| PC:", pc)
