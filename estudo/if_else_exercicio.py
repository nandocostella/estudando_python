# adivinhando o numero secreto

num_sec = int(input("Digite o número secreto: "))

chute = int(input("Digite o número escolhido entre 1 e 10: "))

if num_sec == chute:
    msg_correta = f"Você acertou. O número secreto é {num_sec}"
    print(msg_correta)
else:
    msg_errada = f"Você não acertou o número. O número correto era {num_sec}."
    print(msg_errada)