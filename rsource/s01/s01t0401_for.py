import time

# Funcion que suma los
# primeros "n" numreso naturles
def sum_of_n(n):
    total_sum = 0
    # Sumando los "n" numeros
    # Ciclo for
    for number in range(1,n+1):
        total_sum = total_sum + number
    # Retornando el total de la suma
    return total_sum

# Variable para guardar
# El data set
dataset = []

for repetition in range(1,11):
    # ⏱️ Tomo el tiempo 1 (inicial)
    timestamp_01 = time.time()

    # Sumo los "n" números
    n = repetition*500
    # Guardo el resultado en result
    result = sum_of_n(n)

    # ⏱️ Tomando el tiempo final
    timestamp_02 = time.time()

    # Calculando el tiempo
    elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)

    # Agregar la tripleta de los
    # datos al dataset
    dataset.append( (n,elapsed_time,result) )

# Imprimir el dataset
for tup in dataset:
    print(tup)