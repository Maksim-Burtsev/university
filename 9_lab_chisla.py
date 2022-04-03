import math
import numpy as np
import copy


def weights_and_vectors():
    """Вычисляет наибольшее собственное значение матрицы и её собственные векторы"""

    a = np.array([[5, -4], [7, 6]])

    weights, vectors = np.linalg.eigh(a)

    print(f'Наибольшее собственное значение матрицы = {max(weights)}\n')
    print(f'Наименьшее собственное значение матрицы = {min(weights)}\n')

    print('Векторы для собственных чисел:\n')
    for vector in vectors:
        print(vector)


def isCorrectArray(a):
    for row in range(0, len(a)):
        if(len(a[row]) != len(b)):
            print('Не соответствует размерность')
            return False

    for row in range(0, len(a)):
        if(a[row][row] == 0):
            print('Нулевые элементы на главной диагонали')
            return False
    return True


def isNeedToComplete(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += (x_new[k] - x_old[k]) ** 2
        sum_low += (x_new[k]) ** 2

    return math.sqrt(sum_up / sum_low) < eps


def method_vrasheniy():

    global a, b

    a = [[10, 1, -1],
         [1, 10, -1],
         [-1, 1, 10]]

    b = [11, 10, 10]
    if(not isCorrectArray(a)):
        print('Ошибка в исходных данных')
    else:
        count = len(b)
        x = [1 for k in range(0, count)]

        numberOfIter = 0
        MAX_ITER = 100
        while(numberOfIter < MAX_ITER):

            x_prev = copy.deepcopy(x)

            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if(j != k):
                        S = S + a[k][j] * x[j]
                x[k] = b[k]/a[k][k] - S / a[k][k]

            if isNeedToComplete(x_prev, x):
                break

            numberOfIter += 1

        print(f'Количество итераций на решение: {numberOfIter}')

        print(f'Собственные числа: {x}')


if __name__ == '__main__':
    weights_and_vectors()
    # method_vrasheniy()
