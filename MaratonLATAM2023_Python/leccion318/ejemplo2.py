# Se leen dos números

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande

if numero1 > numero2:
    mayor_numero = numero1
else:
    mayor_numero = numero2

# Imprime el resultado

print("El número mayor es: ", mayor_numero)