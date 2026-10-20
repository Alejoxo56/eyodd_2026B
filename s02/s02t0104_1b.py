# Eliminación
# Importando funcion array del modulo array y renombrandola como arr
from  array import array as arr
# Importando una funcion desde otro archivo
# Archivo
from s02t0102_1D import print_array

my_array = arr('i', [5, 10, 15, 20, 10])

print("---ANTES DE LA ELIMINACION---")
print_array(my_array)

# Eliminación
try:
    my_array.remove(100)
except:
    
    print(f"El elemento no se encuentra en el arreglo")
my_array.remove(100)
print("---DESPUÉS DE LA ELIMINACION---")
print_array(my_array)