# Variables.

print("ejemplo 1.")
var = 1
print(var)

print("ejemplo 2.")
var = 1
balance_cuenta = 10000.0
nombre_cliente = 'Jose Marquez'
print(var, nombre_cliente , balance_cuenta)

print("ejemplo 3.")
var = 1
print(var)
var = var + 1
print(var)

print("ejemplo 4.")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

print("ejemplo 5.")
juan = 3
maria = 5
pablo = 6
print(juan, maria, pablo, sep=',')
total_manzanas = juan + maria + pablo
print(total_manzanas)

print("ejemplo 6.")
kilometros = float(input("ingrese los kilometros: "))
millas = float(input("ingrese las millas: "))

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(kilometros, "kilómetros son", round(kilometros_a_millas, 2), "millas")
print(millas, "millas son", round(millas_a_kilometros, 2), "kilómetros")