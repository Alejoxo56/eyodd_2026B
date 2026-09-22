"""
Escribir un programa que calcule la suma de los "n" numeros naturales. Por ejemplo si n= 100, el programa calculara la suya del 1 al 100

"""
# Importamos  biblioteca 
import time
#Tomando el tiempo incial
# Creando una marca de tiempo 
timestamp_01 = time.time()

# Programa que calcula las suma # de los "n" numeros naturales 
n = 100
sum = 0

# Ciclo for
for number in range (1,n+1):
   sum = sum + number
   # 1: sum <-0 + 1
   # sum = 1
   # 2: sum <- 1 + 2
   # sum = 3 
   #3: sum <- 3 + 3
   # ...
   # 100: sum <- anterior a Sum(o se pone sum_(-1)) + 100 
print(f"La suma de 1 hasta {n} es: {sum}")

# Tomando el tiempo final 
timestamp_02 = time.time()

# Impresion del tiempo de ejecución 
print(f"Tiempo de ejecución: {(timestamp_02 - timestamp_01) * 1e6:.2f} μs")