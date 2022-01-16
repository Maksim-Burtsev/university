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

    a_new = math.e**((lny-lnx*b)/N)
    b_new = (lnxy-lnx*math.log(a))/(lnx2)

    return a_new, b_new
    

N = 20 #число экспериментов
sigma = 3 #стандартное отклонение наблюдаемых значений
a = 2 #теоретическое значение а
b = 2 #теоретическое значение b


f = np.array([a*(i**b) for i in range(1, N+1)])

x_i = np.linspace(1,21, N)
y_i = np.array([a*(i**b)+ random.randint(2, 3) for i in x_i])


x = np.array(range(N))

print(consider_a_b()) #вывод коэффицентов, которые мы получили с использованием практических данных

plt.scatter(x_i, y_i, s=4, color='red')
# # plt.plot(x, f)
plt.show()