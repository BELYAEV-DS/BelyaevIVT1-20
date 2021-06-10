from determinant import determinant
import pandas as pd


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Введите размерность квадратной матрицы (n), чтобы посчитать ее определитель: '))
            matrix = [list() for x in range(n)]

            print('Заполните поля матрицы: ')

            for i in range(n):
                for j in range(n):
                    el = int(input(f'{i}{j}-ый элемент: '))
                    matrix[i].append(el)

            print('Ваша матрица: ')
            print_matrix = pd.DataFrame(matrix)
            print(print_matrix)

            print(f'Детерминант: {determinant(matrix)}')
            if input('Хотите выйти y/n: ') == 'y':
                break
        except ValueError:
            print('Вы ввели неправильное значение, попробуйти занова.')
