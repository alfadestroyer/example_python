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

# Ejercicio con funcion max()
print("Ejemplo con la funcion max().")
print("Ejemplo 2.2.")

numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))
 
numero_mayor = max(numero_1, numero_2, numero_3)
 
print("El número mayor es: ", numero_mayor)

# Ejercicio con funcion min()
print("Ejemplo con la funcion min().")
print("Ejemplo 2.3.")

numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))
 
numero_menor = min(numero_1, numero_2, numero_3)
 
print("El número menor es: ", numero_menor)

# Ejercicio con funcion round().

print("Ejercicio con funcion round()")
print("Ejemplo calculo de impuesto anual")

ingreso_anual = float(input("Introduce el ingreso anual: "))

if ingreso_anual < 85528:
	impuesto_anual = ingreso_anual * 0.18 - 556.02
else:
	impuesto_anual = (ingreso_anual - 85528) * 0.32 + 14839.02

if impuesto_anual < 0.0:
	impuesto_anual = 0.0

impuesto_anual = round(impuesto_anual, 0)
print("El impuesto anual es: ", impuesto_anual, "pesos")

# Ejercicio para definir un año bisiesto

print("Ejercicio para definir un año bisiesto")
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")	
 