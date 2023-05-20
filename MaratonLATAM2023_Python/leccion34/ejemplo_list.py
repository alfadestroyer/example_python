# Ejemplo de listas.


# Ejemplo 1.
print("Ejercicio 1, lista")
print()
# Paso 1: crear una lista vacía llamada beatles
beatles = []

# Paso 2: emplear el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3: emplear el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe y Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)

# Paso 4: usar la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista
del beatles[3]
del beatles[3]

# Paso 5: usar el método insert() para agregar a Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")

print(beatles)
print()

# Ejemplo 2.
print("Ejercicio 2, encontrar el valor mayor en la lista ")
print()

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
print()

# Ejemplo 2.1.
print("Ejercicio 2.1, encontrar el valor mayor en la lista ")
print()

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)
print()

# Ejemplo 3.
print("Ejercicio 3, Ubicación de un elemento dado dentro de una lista")
print()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
print()

# Ejemplo 4.
print("Ejercicio 4, para eliminar elementos repetidos en una lista.")
print()

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []

for number in my_list:
    if number not in new_list:
        new_list.append(number)
my_list = new_list 

print("La lista con elementos únicos:")
print(my_list)


my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])