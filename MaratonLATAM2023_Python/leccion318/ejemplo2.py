# Se leen dos números
print("Ejemplo con el uso de condicionadores if_else")

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande

if numero1 > numero2:
    mayor_numero = numero1
else:
    mayor_numero = numero2

# Imprime el resultado

print("El número mayor es: ", mayor_numero)

# Otra forma aceptada por Python.

print("Ejemplo con el uso de condicionadores if_else")

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 > numero2: mayor_numero = numero1
else: mayor_numero = numero2

print("El número mayor es: ", mayor_numero)
