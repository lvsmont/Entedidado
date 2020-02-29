'''

Jogo ENTEDIDADO
Criado por: Lucas V S Monteiro
GitHub: https://github.com/lvsmont

'''
import os
import random
import sys

def cls():
    try:
        os.system('CLS')
    except:
        os.system('clear')

dado = [1, 2, 3, 4, 5, 6]
reset = "n"

while (reset == "n"):
    cls()
    print("   ***   ENTEDIDADO   ***\n----------------------------\n")
    print("Escolha um modo de jogo.\n")
    print("1) High or Low")
    print("9) Sair do jogo...")

    try:
        game = int(input("\nDigite sua escolha: "))
    except ValueError:
        input("Opção incorreta! Pressione ENTER e tente novamente...")
        game = 0
        reset = "n"

    if (game == 1):
        reset = "s"
        while (reset == "s"):
            cls()
            resultado = random.choice(dado)
            print("Modo de jogo: High or Low\n-------------------------")
            print("Para este modo de jogo, são considerados os números: High (H - 4,5,6) e Low (L - 1,2,3)\n\n")
            escolha = input("Digite 'H' para High ou 'L' para Low: ")

            if (escolha == 'l' or escolha == 'L'):
                print("Resultado:", resultado)
                if (resultado == 1 or resultado == 2 or resultado == 3):
                    print("Você VENCEU!")
                elif (resultado == 4 or resultado == 5 or resultado == 6):
                    print("Você PERDEU...")

            if (escolha == 'h' or escolha == 'H'):
                print("Resultado:", resultado)
                if (resultado == 4 or resultado == 5 or resultado == 6):
                    print("Você VENCEU!")
                elif (resultado == 1 or resultado == 2 or resultado == 3):
                    print("Você PERDEU...")

            elif (escolha != 'h' and escolha != 'l' and escolha != 'H' and escolha != 'L'):
                print("Opção inválida! Digite o valor correto.")

            reset = input(("\nDeseja jogar novamente? (s) SIM ou (n) Não:"))

            if (reset != 's' and reset != 'n'):
                input("Opção incorreta! Pressione ENTER para ser redirecionado ao menu...")
                game = 0
                reset = "n"

    elif (game == 9):
        cls()
        print("Obrigado por jogar! Até logo.\n")
        input("Pressione ENTER para fechar o jogo...")
        sys.exit()
