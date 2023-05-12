# Ejemplo 1.
print("Ejemplo 1")
print("Dime lo que sea...")
dime_algo = input()
print("Hmm...", dime_algo, "... ¿en serio?")

# Ejemplo 2.
print("Ejemplo 2")
ingreso_numero = float(input("Ingresa un número: "))
salida_numero = ingreso_numero ** 2.0
print(ingreso_numero, "al cuadrado es", salida_numero)

# Ejemplo 3.
print("Ejemplo 3.1")
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

print("Ejemplo 3.2")
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)