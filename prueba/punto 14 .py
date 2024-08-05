def aritmetica(lista):
    if not lista:
        return None  
    
    suma = sum(lista)
    cantidad = len(lista)
    media = suma / cantidad
    
    return media

lista_numeros = [10, 20, 30, 40, 50]
media = aritmetica(lista_numeros)

print(f"La media aritmética es: {media:.2f}")
