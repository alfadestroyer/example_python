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

print("Ejemplo 3.3")
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))

# Ejemplo 4.
print("Ejemplo 4.")
nombre = input("¿Me puedes dar tu nombre por favor? ")
apellido = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + nombre + " " + apellido + ".")

# Ejemplo 5.
print("Ejemplo 5.")
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

# Ejemplo 6.
print("Ejemplo 6.")
horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))
minutos = minutos + duracion # encuentra el número total de minutos
horas = horas + minutos // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
minutos = minutos % 60 # corrige los minutos para que estén en un rango de (0..59)
horas = horas % 24 # corrige las horas para que estén en un rango de (0..23) 
print(horas, ":", minutos, sep='')