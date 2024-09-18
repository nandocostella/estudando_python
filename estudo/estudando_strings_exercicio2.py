frase = "Python é uma linguagem de programação poderosa e versátil"

# Conta todos os caracteres da frase
contagem = frase.count("")
contagem_dois = len(frase)
print(contagem_dois)
print(contagem)

# imprime a primeira palavra da frase
palavra = frase[:6]
print(palavra)

# converte a frase em letras maiúsculas
frase_maiuscula = frase.upper()
print("Frase em maiúscula:", frase_maiuscula)

# Substitui a palavra Poderosa pela palavra Incrível
frase_substituida = frase.replace("poderosa", "incrível")
print("Frase com substituição: ", frase_substituida)