#importando el modulo arrays
from array import array as arr

#creando un array de enteros
#i: entero con signo
#I: entero sin signo
#f: numero decimal
#d: numer odecimal doble
#u caracteres umicodes 
my_array = arr('i', [200, 300, 400, 500,600, 700, 800, 900, 1000]) # O(1)

# iteracion automatica 
for num in my_array: 
    print(num)

#accso individual a elementos 
print(my_array[0])
print(my_array[1])
print(my_array[2])


print(len(my_array))

for i in range(len(my_array)):
    if my_array[i] % 2 == 0:
     print(f"elememto {i+1}: {my_array{i}}")