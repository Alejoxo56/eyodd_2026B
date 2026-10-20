from array import array as arr 

#im´presioin de una tabla 
def print_table(input_table):
    #importamos cada elemento
    for row in input_table:
        for column in row:
            print(column, end=", ")
        print("\n")  
 

table = [arr('i', [1,2,3]),
         arr('i', [4,5,6]),
         arr('i', [7,8,9])]

print_table(table)

#imserccion 
row = 1 
column = 2
value = 99

# insertar en la fila 1 l ac columna 2 el valor 99
table [row].insert(column, value)
#imprimendo mensaje 


#insertando un fila completa 
new_raw = arr('i', [10,11,12])
pos = 3
table.insert(pos, new_raw)
print_table("---después de la inserción de una fila completa---")
print_table(table)

#eliminacion de elementos 

del table[2]
print_table("---después de la eliminación---")
print_table(table)