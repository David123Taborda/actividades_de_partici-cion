def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

grados_fahrenheit = 98.6
grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
print(f"{grados_fahrenheit} grados Fahrenheit son {grados_celsius:.2f} grados Celsius.")
