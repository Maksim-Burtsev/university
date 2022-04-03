import numpy as np


def shooting():
    alpha = np.log(8*(np.pi**2))
    beta = np.log(8*(np.pi**2))

    def equation(t):
        c1 = (8*(np.pi**2))
        c2 = 0
        sol = np.log(c1) - 2*np.log(np.cos(0.9939931166*t) + c2)
        return sol

    i = 0
    solution = []
    valset = []

    def newZ(a, A, b, B):
        VAL = a + (beta - A)*((a - b) / (A - B))
        return VAL

    Z = (-23/2)
    Zm1 = (-25/2)

    valset.append(Zm1)
    valset.append(Z)

    while i < 11:
        VAL = newZ(Z, equation(Z), Zm1, equation(Zm1))

        Zm1 = Z
        Z = VAL

        i += 1

        valset.append(VAL)

        solution.append(equation(Z))

    print("\nРезультаты метода стрельбы")
    print("====================================================\n")
    print("   Z-значение                 Решение")

    for i in range(0, 2):
        print(" ", valset[i], " \t\t", solution[i])

    for i in range(2, 11):
        print(" ", valset[i], " \t", solution[i])

    print(f"\nРешение: {alpha}")
    print("====================================================\n")


def progonka():
    # Пробные данные для уравнения A*X = B
    a = [[10.8000, 0.0475,      0, 0],
         [0.0321, 9.9000, 0.0523, 0],
         [0, 0.0369, 9.0000, 0.0570],
         [0,      0, 0.0416, 8.1000]]

    b = [12.1430, 13.0897, 13.6744, 13.8972]

    # Решение, которое должно получиться:
    # x1 = 1,118587
    # x2 = 1,310623
    # x3 = 1,503186
    # x4 = 1,707983

    # Вывод матрицы на экран

    def print_arr(string, namevec, a):
        if (type(a) == int) or (type(a) == float):
            print(a)
        else:
            print(string)
            for k in range(len(a)):
                print("{}[{}] = {:8.4f}".format(namevec, k, a[k]))

    # Проверка 3х-диаг. матрицы коэффициентов на корректность

    def isCorrectArray(a):
        n = len(a)

        for row in range(0, n):
            if(len(a[row]) != n):
                print('Не соответствует размерность')
                return False

        for row in range(1, n - 1):
            if(abs(a[row][row]) < abs(a[row][row - 1]) + abs(a[row][row + 1])):
                print('Не выполнены условия достаточности')
                return False

        if (abs(a[0][0]) < abs(a[0][1])) or (abs(a[n - 1][n - 1]) < abs(a[n - 1][n - 2])):
            print('Не выполнены условия достаточности')
            return False

        for row in range(0, len(a)):
            if(a[row][row] == 0):
                print('Нулевые элементы на главной диагонали')
                return False
        return True


    def solution(a, b):
        if(not isCorrectArray(a)):
            print('Ошибка в исходных данных')
            return -1

        n = len(a)
        x = [0 for _ in range(0, n)]  
        print('Размерность матрицы: ', n, 'x', n)

        v = [0 for k in range(0, n)]
        u = [0 for k in range(0, n)]

        v[0] = a[0][1] / (-a[0][0])
        u[0] = (- b[0]) / (-a[0][0])
        for i in range(1, n - 1):

            v[i] = a[i][i+1] / (-a[i][i] - a[i][i-1]*v[i-1])
            u[i] = (a[i][i-1]*u[i-1] - b[i]) / (-a[i][i] - a[i][i-1]*v[i-1])

        v[n-1] = 0
        u[n-1] = (a[n-1][n-2]*u[n-2] - b[n-1]) / \
            (-a[n-1][n-1] - a[n-1][n-2]*v[n-2])

        print_arr('\nПрогоночные коэффициенты v: ', 'v', v)
        print_arr('\nПрогоночные коэффициенты u: ', 'u', u)

        x[n-1] = u[n-1]
        for i in range(n-1, 0, -1):
            x[i-1] = v[i-1] * x[i] + u[i-1]

        return x

    x = solution(a, b)
    print_arr('\nРешение: ', 'x', x)


if __name__ == '__main__':
    shooting()
    # progonka()
