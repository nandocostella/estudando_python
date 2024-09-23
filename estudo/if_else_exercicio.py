# adivinhando o numero secreto

num_sec = int(input("Digite o número secreto: "))

num_escolhido = int(input("Digite o número escolhido entre 1 e 10: "))

if num_sec == num_escolhido:
    msg = f"Você acertou. O número secreto é {num_sec}"
    print(msg)
else:
    print("Você não acertou o número. Tente novamente")