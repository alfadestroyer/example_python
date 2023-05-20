# Ejemplo de bucles

# Ejemplo 1.
print("Ejemplo 1 de bucle con while.")

# Almacena el actual número más grande aquí.
numero_mayor = -999999999
 
# Ingresa el primer valor.
numero = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if numero > numero_mayor:
        # Sí si, se actualiza largest_number.
        numero_mayor = numero
    # Ingresa el siguiente número.
    numero = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", numero_mayor)

# Ejemplo dos.
print("Ejemplo 2 de bucle con while.")

# Depura las variable igualandolas a (0).
numero_impar = 0
numero_par = 0
 
# Lee el primer número.
numero = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while numero != 0:
    # Verificar si el número es impar.
    if numero % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        numero_impar += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        numero_par += 1
    # Leer el siguiente número.
    numero = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", numero_impar)
print("Conteo de números pares:", numero_par)


# Ejemplo 3.
print("Ejemplo 3 de bucle con while y uso de variable para salir.")
contador = 5
while contador != 0:
    print("Dentro del bucle.", contador)
    contador -= 1
print("Fuera del bucle.", contador)

 
# Ejemplo 4.
print("Ejemplo 4 de bucle.")
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


# Ejemplo 5.
print("Ejemplo 5 de bucle.")

numero_secreto = 777
print(
 """
 +================================+
 | ¡Bienvenido a mi juego, muggle!|
 | Introduce un número entero     |
 | y adivina qué número he        |
 | elegido para ti.               |
 |¿Cuál es el número secreto?     |
 +================================+
 """)

numero_entero = int(input("Ingresa un numero entero y juega: "))
 
while numero != 777:
    if numero_secreto == numero_entero:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        numero = 777
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        numero_entero = int(input("Ingresar un nuevo numero entero y juega: "))


# Ejemplo 6.
print("Ejemplo 6 de bucles con for, range().")
for i in range(10):
    print("El valor de i es", i)


# Ejemplo 7.
print("Ejemplo 7 de bucle con for, range() con dos agumentos.")
for i in range(2, 8):
    print("El valor de i es", i)

# Ejemplo 8.
print("Ejemplo 8 de bucle con for, range() con tres agumentos.")
for i in range(2, 8, 3):
    print("El valor de i es", i)
    

# Ejemplo 9.
print("Ejemplo 9 de bucle, ejercicio.")

import time

    # Escribe un bucle for que cuente hasta cinco.
for i in range(1, 6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(i, " Mississippi")
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)
# Escribe una función print con el mensaje final.
print()
print("¡Listos o no, ahí voy!")


# Ejemplo 10.
print("Ejemplo 10 de bucle con for, break y continue.")
    # break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

    # continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# Ejemplo 11.
# break - ejemplo.
print("Ejemplo 11 de bucle con for, break y continue.")
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

# continue - ejemplo.
largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")


# Ejemplo 12.

# break - ejemplo.

palabra_salida = "chupacabra"

while palabra_salida:
    palabra = input("Ingresa una palabra: ")
    if palabra == palabra_salida:
        break
print("Has dejado el bucle con éxito.")


# Ejemplo 13.
print("Ejercicio 1 Devorador de vocales.")

# Indicar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")
# y asignarlo a la variable user_word.
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in "AEIOU":
        continue
    else:
        print(letter)


# Ejemplo 14.
print("Ejercicio 2 Devorador de vocales.")

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")



# y asignarla a la variable user_word.
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter in "AEIOU":
        continue
    else:
        word_without_vowels += letter

# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)


# Ejemplo 15.
print("Ejercicio 3 Calcular la altura de una piramide.")

blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

height = 0
layer_blocks = 1

while layer_blocks <= blocks:
    height += 1
    blocks -= layer_blocks
    layer_blocks += 1
    
# Imprime el resultado.
print("La altura de la pirámide:", height)


# Ejemplo 16.
print("Ejercicio 4 La hipótesis de Collatz")
 
c0 = int(input("Ingresa un número natural: "))

steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("Pasos =", steps)
