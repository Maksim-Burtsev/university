import numpy as np

EXAMPLE = [[8.0, 7.0,   3.0,  18.0],
           [-7.0, -4.0, -4.0, -11.0],
           [-6.0,  5.0, -4.0, -15.0]]


def main():

    n = int(input('Введите количество неизвестных: '))

    a = np.zeros((n,n+1))

    # n = 3
    # a = EXAMPLE

    x = np.zeros(n)

    print('Введите количество коэффицентвов в матрице')
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

    for i in range(n):
        if a[i][i] == 0.0:
            raise ValueError(f'Обнаружено деление на 0! a[{i}][{i}]=0')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    print('\nRequired solution is: ')
    for i in range(n):
        print(f'X{i} = {x[i]:.2f}\t')


if __name__ == '__main__':
    main()
