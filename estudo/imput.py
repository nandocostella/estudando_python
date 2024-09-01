# nome = input("Digite seu nome: ")
# print("\nSeu nome é: ", nome)


usuario = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(usuario, " sua média final é: ", media)

if media < 6:
    print ("Você reprovou")
else:
    print ("Você foi aprovado")