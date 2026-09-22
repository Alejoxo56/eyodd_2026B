"""
escrbir un programa que calcule 
la suma de los "n" numeros naturales.
por elemplo si n= 100, el progama 
calculara la suma de 1 al 100
42

"""
# importamos bliblioteca time
import time

# Crear una marca de tiempo
timestamp_01 = time.time()
# progama que calcule las sumas 
# de los "n" numeros naturales 
n= 100
sum = 0

#ciclo for
for number in range(1,n+1):
    sum = sum + number 
    # l: sum <- 0 + 1
    # sum = 1
    # 2: sum <- 1 + 2 
    # sum = 3 
    # 3: sum <- 3 +3 
    # ...
    # 100: SUM : <- sum_(-1) + 100
    print(f"la sunma de 1 hasta {n} es: {sum}")

    times