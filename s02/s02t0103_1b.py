from array import array as arr 
#importando una funcion de otro archivo
from s02t0102_1d import print_array

my_array = arr('i', [10,22,300,3,7,10,22,42,32,17])

print("---ANTES DE LA INSERCCION---")
print_array(my_array)

#INSERCION 
my_array.insert(3, 100)
print("---DESPUES DE LA INSERCCION---")
print_array(my_array)

print("---DESPUES DE UN APPEND---")
my_array.append(500)
print_array(my_array)

print("---simulando un append con insert---")
my_array.insert(len(my_array), 600)
print_array(my_array)