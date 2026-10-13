'''
Notas:
1. Se identifica el tamaño de la entrada "n". El tamaño de la entrada es
el num. de estudiantes
2. Ver cuanto crece el num. de operaciones en mi algoritmo
conforme crece el tamaño de la  entrada.
3. Se agregan las big O's a cada linea de codigo para identificar el num. de operaciones
Teniendo en cuenta la cota superior asintotica:
O(n) + 4*O(1) = O(n+4) = O(n)
'''

# Creando una lista de estudiantes:)
students_list_01  = ['Juan', 'Pedro', 'Maria', 'Jose']
students_list_02  = ['Yerik', 'María', 'Makunga', 'Alejo']

#Verificando la presencia de un estudiante en la lista
def check_student(input_student, students_list):
    for student in students_list:
        if input_student == student: # big O(n)
            print("Estudiante encontrado") #big O(1)
            return student #big O(1)
        #Sino se encuentra el estudiante, se retorna None
        print("Estudiante no encontrado") #big O(1)
    return None #big O(1)

#Testing
check_student("Alejo", students_list_02)