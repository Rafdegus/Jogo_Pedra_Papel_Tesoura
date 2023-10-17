# Jogo "Pedra Papel Tesoura" V:1.0 #
# Coder: Rafael Gusmão #

import random



# 02 Lógica #
def escolha():
    global Escolha_Jogador
    global pc
    
    Escolha_Jogador = input("Escolhe um (pedra, papel, tesoura): ").lower()
    pc = random.choice(("pedra", "papel", "tesoura"))
    
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
    if Escolha_Jogador == "exit":
        return "exit"
    return ""


# Loop infinito, apenas sai se resultado = exit #
while True:
    # Chamada da função #
    resultado = escolha()
    if resultado != "":
        if resultado == "exit":
            # sai do loop (termina programa) #
            break
        # resultado válido #
        print(resultado)
        print("Jogador:", Escolha_Jogador, "| PC:", pc)
    else:
        # resultado inválido #
        print("Escolha Errada")


