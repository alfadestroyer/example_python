# Se leen dos números
print("Ejemplo con el uso de condicionadores if_else")
print("Ejemplo 1.")
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
print("Ejemplo 1.1.")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 > numero2: mayor_numero = numero1
else: mayor_numero = numero2

print("El número mayor es: ", mayor_numero)

# Ejemplo para comparar tres(3) numneros y definir cual es el mayor.
print("Ejemplo con el uso de condicionadores if_else")
print("Ejemplo 2, de numero mayor con tres condiciones")
# Se leen tres números
numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))
 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
numero_mayor = numero_1
 
# Comprobamos si el segundo número es más grande que el número mayor actual
# y actualiza el número mayor si es necesario.
if numero_2 > numero_mayor:
    numero_mayor = numero_2
 
# Comprobamos si el tercer número es más grande que el número mayor actual
# y actualiza el número mayor si es necesario.
if numero_3 > numero_mayor:
    numero_mayor = numero_3
 
# Imprime el resultado.
print("El número mayor es :", numero_mayor)

# otra forma de realizar el ejercicio
print("Ejemplo con el uso de condicionadores if_else")
print("Ejemplo 2.1.")

numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))
 
if numero_1 > numero_2: numero_mayor = numero_1
else: numero_mayor = numero_2
 
if numero_3 > numero_mayor: numero_mayor = numero_3
 
print("El número mayor es: ", numero_mayor)
