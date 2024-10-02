# elegibilidade para voto

idade_elegivel = 18
idade = int(input("Por favor, digite a sua idade: "))

if idade >= idade_elegivel:
    print("Você é elegível votar!")
else:
    nao_elegivel = f"Você não é elegível para votar. A idade mínima para votação é {idade_elegivel} anos."
    print(nao_elegivel)