#importando el modulo arrays
from array import array as arr

#creando un array de enteros
array_01 = arr('i', [3, 8, 5, 1, 6]) # O(1)

#iterando sobre el array
for data in array_01: # O(n)
    print(data) # O(1)
print()