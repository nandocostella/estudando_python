import random

print(random.randrange(1, 50))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numeros)
print(numeros)
print(random.choice(numeros))
