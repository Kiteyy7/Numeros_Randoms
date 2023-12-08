import random

adivinha = int(input("Tente adivinhar o numero do robo entre 1 e 4: "))
num = random.randint(1, 4)

if adivinha == num:
    print("Voce Acertou o numero do robo!!!")



else:
    print(f"Voce errou o numero do robo!!! ""O Numero era{num}")

