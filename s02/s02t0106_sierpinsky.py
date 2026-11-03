from array import array as arr
from enum import Enum

# Borra pantalla con caracteres ANSI
def clear_screen():
    print("\033[2J\033[H", end="")


# Encapsulado de los colores ANSI
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


# Funcion para generar el triangulo
def generate_triangle(rows=10):

    # Parametros de mi cuadricula
    columns = 2 * rows - 1

    # Creando el grid 2D
    matrix = []

    # Construyendo el grid
    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matrix.append(new_row)

    # Calculando el centro de la primera fila
    center = columns // 2

    # Estableciendo el centro en 1
    matrix[0][center] = 1

    # Se calcula el resto de la matriz
    # Siguiendo la logica del Sierpinski Gasket
    for row in range(1, rows):
        for col in range(0, columns):

            left_upper_cell = 0
            right_upper_cell = 0

            # Validando el borde izquierdo
            if col > 0:
                left_upper_cell = matrix[row-1][col-1]

            # Validando el borde derecho
            if col < columns - 1:
                right_upper_cell = matrix[row-1][col+1]

            # Asignando valor al arreglo
            if left_upper_cell != right_upper_cell:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0

    # Regresando la matriz
    return matrix


# Funcion para dibujar la matriz
def draw_matrix(input_matrix, symbol="*"):

    for row in input_matrix:
        for cell in row:

            if cell == 1:
                print(
                    AnsiColor.CYAN.value +
                    symbol +
                    AnsiColor.RESET.value,
                    end=""
                )
            else:
                print(
                    AnsiColor.RED.value +
                    " " +
                    AnsiColor.RESET.value,
                    end=""
                )

        print()


# Metodo principal
def main():

    # Genera el triangulo de Sierpinski con 10 filas
    matrix = generate_triangle(10)

    # Limpia la pantalla antes de dibujar
    clear_screen()

    # Dibuja la matriz en pantalla
    draw_matrix(matrix, symbol="■")


# Ejecucion del programa principal
if __name__ == "__main__":
    main()

