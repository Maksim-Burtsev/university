import scipy.integrate as spint
import numpy as np
from numpy import cos, sin


def f(i, t):
    return cos(1+2*t)/(1+i*t**2)


def coef(i):
    if (i == 1) | (i == n):
        return 1
    else:
        return -(4+sin(2*i)/(10+i))


def simpson(f, a, b, eps):
    return spint.quad(f, a, b)[0]


def B(i):
    inteps = 0.01

    def F(t):
        return f(i, t)
    return -1+simpson(F, 0, 1, inteps)


n = 1000
A = np.zeros([n, n])

for j in range(0, n):
    A[j][j] = coef(j+1)

for j in range(1, n-1):
    A[j][j-1] = A[j][j+1] = 1

b = np.ones(n)
for j in range(1, n-1):
    b[j] = B(j+1)

x = b
eps = 0.001
xold = b+10*eps
E = np.identity(n)

N = 0
while np.linalg.norm(x-xold)/np.linalg.norm(xold) > eps:
    N += 1
    r = A@x-b
    tau = ((A@r)@r)/((A@r)@(A@r))
    xold = x
    x = (E-tau*A)@x+(tau*E)@b

print(f'Число итераций {N}')
print(f'Ответ {np.linalg.norm(x)}')
# print(np.linalg.norm(np.linalg.solve(A,b)))
