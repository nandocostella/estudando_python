# Imprime parte do texto conforme posição de cada letra
posicaoLetra = ("Python")

print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])
print(posicaoLetra[5])


frase = "Olá, mundo"

parte = frase[4:8]
print(parte) # imprime da posição 4 até a 8

primeiros = frase[:5]
print(primeiros) # imprime as 5 primeiras posições

ultimos = frase[-5:]
print(ultimos) # imprime os últimos 5 caracteres da string



# o comando "in" verifica se a string passada está na frase maior
frase2 = "Estudando o modulo de python"
print("python" in frase2)

# verifica se a palavra python está na frase e imprime o texto
if "python" in frase2:
    print("A palavra esta na frase")


# usado o strip para remover espaços em branco no inicio e final da frase
frase3 = "       Estudando o modulo de python            "
print(frase3.strip())

# remove o caractere usado passado como parâmetro
texto = "*******Olá!*************"
texto_strip = texto.strip('*')
print(texto_strip)

# usado split para quebrar a frase em várias frases
palavras = frase3.split()
print(palavras)

# o join junta a lista de palavras em uma frase e separa pelo espaço
junta = ' '.join(palavras)
print(junta)

