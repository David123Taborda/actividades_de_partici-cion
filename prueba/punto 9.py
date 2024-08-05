filas = 3
columnas = 3

contador = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(contador)
        contador += 1
    print(" ".join(map(str, fila)))
