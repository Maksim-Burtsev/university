import numpy as np


EXAMPLE = [[1, 1, 3],
           [1, 3, -3],
           [-2, -4, -4]]

def main():
    # n = int(input('Введите количество неизвестных: '))

    n = 3
    a = np.zeros((n,2*n))

    for i in range(len(EXAMPLE)):
        for j in range(len(EXAMPLE[i])):
            a[i][j] = float(EXAMPLE[i][j])

    # print('Введите коэффиценты матрицы')
    # for i in range(n):
    #     for j in range(n):
    #         a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

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

if __name__ == '__main__':
    main()