from array import array as arr

#parametros de mi cuadricula
row = 8
columns = 2 * rows -1

#creando el grid 2d
matrix = []
#construyendo el grid
for _ in range (rows):
    new_row = arr("1",[0] * columns)
matrix.append(new_row)

#validando la construccion del grid
print(f"cantidad de filas: {len (matrix)}")
print(f"cantidad de columnas: {len (matrix[0])}")

for row in matrix:
    print(list(row))





