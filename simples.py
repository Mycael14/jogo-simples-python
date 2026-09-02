
import random

pontuacao = 0

while True:

    numero = random.randint(1, 5)

    chute = int(input("Escolha um número de 1 a 5: "))

    if chute == numero:
        print("Você acertou!!!")

        pontuacao += 1

        print(f"Pontuação atual: {pontuacao}")

    else:
        print("Você errou!!!")

        print(f"Computador: {numero}, seu chute: {chute}")

    jogar_novamente = input("Quer jogar novamente? (s/n): ")

    if jogar_novamente.lower() != "s":
        print(f"Jogo encerrado! Pontuação final: {pontuacao}")
        break









