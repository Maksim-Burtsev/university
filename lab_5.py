import numpy as np
import matplotlib.pyplot as plt
import random
import math

def consider_a_b():
    global x_i, y_i, N, b
    lnx = sum(np.log(x_i)) #тут сумма lnxi
    lny = sum(np.log(y_i)) #тут сумма lnyi
    lnx2 = sum(map(lambda x: (x)**2, np.log(x_i))) #тут сумма lnxi2
    lnxy = sum([np.log(x_i)[i]*np.log(y_i)[i] for i in range(N)]) #тут сумма lnxi*lnyi
    
    m_list =  [[N, lnx], [lnx, lnx2]]
    A = np.array(m_list)
    inv_A = np.linalg.inv(A)
    B = np.array([lny, lnxy])
    X = np.linalg.inv(A).dot(B)
    
    a_new = math.e**X[0]
    b_new = X[1]
    print(a_new, b_new)

    return a_new, b_new
    



# x_i = [1, 2, 3, 4, 5, 3, 4, 13]
# y_i = [1, 3, 2, 4, 6, 7, 8, 2]
x_i = [i for i in range(1, 15)]
y_i = [i**3 if i%2 == 1 else i**2 for i in x_i]

# y_i = [i**2 + random.randint(0, i**2) for i in x_i]

N = len(x_i)

a_new, b_new = consider_a_b()
n_array = np.linspace(0, N, 100)
f_new = np.array([a_new*(i**b_new) for i in n_array])
plt.scatter(x_i, y_i, s=4, color='red')
plt.plot(n_array, f_new)
plt.show()

def n_1():
    N = 100    # число экспериментов
    sigma = 3   # стандартное отклонение наблюдаемых значений
    k = 0.5     # теоретическое значение параметра k
    b = 2       # теоретическое значение параметра b

    x = np.array(range(N))
    f = np.array([k*z+b for z in range(N)])
    y = f + np.random.normal(0, sigma, N)

    # вычисляем коэффициенты
    mx = x.sum()/N 
    my = y.sum()/N  
    a2 = np.dot(x.T, x)/N 
    a11 = np.dot(x.T, y)/N  #перв_нач_мом

    kk = (a11 - mx*my)/(a2 - mx**2)
    bb = my - kk*mx
    print(kk, bb)
    ff = np.array([kk*z+bb for z in range(N)])

    plt.scatter(x, y, s=2, c='red')
    # plt.plot(f)
    plt.plot(ff, c='red')
    plt.grid(True)
    plt.show()

# n_1()