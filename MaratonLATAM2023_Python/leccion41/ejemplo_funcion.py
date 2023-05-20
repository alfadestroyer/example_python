# Uso de funciones.
# Ejemplo de uso de funciones.


# Ejemplo 1.
print("Ejercicio 1. definir los años bisiestos.")
print()
def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

    
# Ejemplo 2.
print()
print("Ejercicio 2, calculo de la Masa corporal.")
print()
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(52.5, 1.65))


# Ejemplo 3.
print()
print("Ejercicio 3, funciones: Triángulos.")
print()

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Ejemplo 3.1.
print()
print("Ejercicio 3.1, funciones: Triángulos, codigo mas compacto.")
print()

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
  
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Ejemplo 3.2.
print()
print("Ejercicio 3.2, funciones: Triángulos, codigo mas compacto.")
print()

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Ejemplo 3.3.
print()
print("Ejercicio 3.3, funciones:Triángulos y el Teorema de Pitágoras.")
print()

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')


# Ejemplo 3.3.1.
print()
print("Ejercicio 3.3.1,funciones:Triángulos y el Teorema de Pitágoras.")
print()

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
  
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
  
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
  
print(area_of_triangle(1., 1., 2. ** .5))
print()


# Ejemplo 4.
print()
print("Ejercicio 4,funciones: Factoriales.")
print()

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
  
for n in range(1, 6): # probando
    print(n, factorial_function(n))
print()


# Ejemplo 5.
print()
print("Ejercicio 5,funciones: Números Fibonacci.")
print()

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
  
for n in range(1, 10):
    print(n, "->", fib(n))
print() 


# Ejemplo 6.
print()
print("Ejercicio 6,funciones: factorial-recursividad.")
print()

def factorial(n):
    if n == 1: # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24
print() 


# Ejemplo 7.
print()
print("Ejercicio 7,funciones: Números Fibonacci-recursividad.")
print()

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))
print() 


# Ejemplo 8.
print()
print("Ejercicio 8, Tuplas.")
print()

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
print() 


# Ejemplo 9.
print()
print("Ejercicio 9, Tuplas y Diccionarios.")
print()

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
print() 
