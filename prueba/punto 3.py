import random

cantidad = 10
limiteabajo = 1
limitearriba = 100

numeros_aleatorios = [random.randint(limiteabajo, limitearriba) for _ in range(cantidad)]

print("números aleatorios:")
print(numeros_aleatorios)
