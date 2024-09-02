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


nome = ("Alice")
idade = 25
altura = 1.65522

# usando o "f" antes da string significa que posso passar algumas variáveis dentro da strint usando as chaves
mensagem = f"Olá, meu nome é {nome}. Tenho {idade} anos e minha altura é {altura:.2f} metros" # ".2f": usado para limitar a 2 caracteres
print(mensagem)


# Formatar pra maiúscula e minúscula no texto
texto2 = "Olá o mundo"
texto_upper = texto2.upper()
print(texto_upper)

texto_lower = texto2.lower()
print(texto_lower)

# deixa apenas a primeira letra do texto em maiúscula
texto_capitalize = texto2.capitalize()
print(texto_capitalize)

# conta as ocorrências de uma letra ou termo
ocorrencia = texto2.count("o")
print(ocorrencia)


substitui_texto = texto2.replace("mundo", "amigo")
print(substitui_texto)