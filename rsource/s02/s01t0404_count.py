# Se crea una lista de estudiantes
students_list_01 = ['Juan', 'Pedro', 'Maria', 'Jose']  # O(n) porque depende de la 
                                                        # cantidad de elementos


def random_function(students):
    first = students[0]  # O(1)
    total = 0  # O(1)
    new_list = []  # O(1)

    for student in students:  # O(n)
        total += 1  # O(1)
        new_list.append(student)  # O(1)
        print(new_list)  # O(1) para una sola impresión

    return total  # O(1)

print(random_function(students_list_01))  # O(n) porque la funcion recorre toda la lista