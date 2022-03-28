import numpy as np


def first_task():
    """Решение системы"""
    n = 3
    a = np.array([[1, -1, 3, 8],
                  [3, 5, -1, 6],
                  [2, 1, -2, -1]])
    x = np.zeros(n)

    for i in range(n):
        if a[i][i] == 0.0:
            raise ValueError(f'Обнаружено деление на 0! a[{i}][{i}]=0')

        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2, -1, -1):
        x[i] = a[i][n]

        for j in range(i+1, n):
            x[i] = x[i] - a[i][j]*x[j]

        x[i] = x[i]/a[i][i]

    print('\nРешение: ')
    for i in range(n):
        print(f'X{i} = {x[i]:.2f}\t')


def second_task():
    """Нахождение обратной матрицы"""
    array = np.array([[1, -1, 3],
                      [3, 5, -1],
                      [2, 1, -2]])
    n = 3
    a = np.zeros((n, 2*n))

    for i in range(len(array)):
        for j in range(len(array[i])):
            a[i][j] = float(array[i][j])

    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = float(a[i][j])

    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j+n] = 1

    for i in range(n):
        if a[i][i] == 0.0:
            raise ValueError(f'Обнаружено деление на 0! a[{i}][{i}]=0')

        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(2*n):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    for i in range(n):
        divisor = a[i][i]
        for j in range(2*n):
            a[i][j] = a[i][j]/divisor

    print('\nОБРАТНАЯ МАТРИЦА:')
    for i in range(n):
        for j in range(n, 2*n):
            print(a[i][j], end='\t')
        print()


def third_ex():
    """Наибольшее собственное значение матрицы"""
    array = np.array([[1, -1, 3],
                      [3, 5, -1],
                      [2, 1, -2]])

    w, _ = np.linalg.eig(array)

    print(max(w))


def evklid_norm():

    array = np.array([[1, -1, 3],
                      [3, 5, -1],
                      [2, 1, -2]])

    evklid = 0
    for i in np.arange(3):
        for j in np.arange(3):
            evklid = evklid + np.sum(np.power(np.abs(array[i, j]), 2))

    print(f'Евклидова норма = {np.sqrt(evklid)}')


def first_norm():

    array = np.array([[1, -1, 3],
                      [3, 5, -1],
                      [2, 1, -2]])

    colsums = []
    for i in np.arange(3):
        v = np.sum(np.abs(array[:, i]))
        colsums.append(v)

    print(f'первая норма = {np.max(colsums)}')


def m_norma():
    array = np.array([[1, -1, 3],
                      [3, 5, -1],
                      [2, 1, -2]])

    rowsums = []
    for i in np.arange(3):
        v = np.sum(np.absolute(array[i, :]))
        rowsums.append(v)

    print(f'm-норма = {np.max(rowsums)}')


def four_task():
    evklid_norm()
    first_norm()
    m_norma()


first_task()
# second_task()
# third_ex()
# four_task()
