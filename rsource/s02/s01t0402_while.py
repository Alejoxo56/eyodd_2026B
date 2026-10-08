"""
Escribir un programa que calcule
la suma de los "n" numeros naturales.
Por ejemplo si n= 100, el programa
calculara la suma de 1 al 100
42
"""

# importar la biblioteca de tiempo
import time

# variable para guardar El data set
dataset = []

# 10 mediciones
for repetition in range(1, 11):
    
    # variables para el problema 
    # se multiplica por 500 para obtener: 500, 1000, 1500 ... 5000
    n_original = repetition * 500
    n = n_original # se copia el valor porque while modificará 'n'
    
    # como ya existe sum en py, se cambiara el name
    the_sum = 0

    # tiempo 1
    timestamp_01 = time.time()

    # iniciando la suma
    while(n > 0):
        the_sum = the_sum + n
        # se busca que n + (n-1) + (n-2) ... + 1
        n = n - 1

    # tiempo 2
    timestamp_02 = time.time()

    # se calcula el tiempo
    elapsed_time = round((timestamp_02-timestamp_01) * 1e6, 2)
    
    # agregar la tripleta de los datos al dataset
    dataset.append( (n_original, elapsed_time, the_sum) )

# dataset
for tup in dataset:
    print(tup)