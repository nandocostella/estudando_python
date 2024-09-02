nome = "Maria"
sobrenome = "Silva"
idade = 30

nome_completo = nome + " " + sobrenome
print(nome_completo)

# abaixo duas formas de tratar as strings
mensagem = f"Ola, senhora {nome_completo} ou podemos chama-la apenas de {nome}. A idade que você informou foi {idade}"
mensagem2 = "Ola, senhora {} ou podemos chama-la apenas de {}. A idade que você informou foi {}".format(nome_completo, nome, idade)
print(mensagem)
print(mensagem2)