texto = input("Ingresa una cadena de texto: ")

texto_bien= texto.replace(" ", "").lower()

if texto_bien== texto_bien[::-1]:
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")
