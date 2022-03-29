import scipy.integrate as spint
from numpy import cos, sin, exp
import numpy as np
from numpy.linalg import norm


def f(i, t):
    return exp(-i**2*t**2)/(1+i*t*cos(t)**2+t**2)


def coef(i):
    if (i == 1) | (i == n):
        return 1
    else:
        return -(4+sin(2*i)/(10+i))


def Int(m):
    a = 0
    b = 1

    def F(t):
        return f(m, t)

    def f38(a, b):
        return (b-a)/8*(
            F(a) +
            3*F((2*a+b)/3) +
            3*F((a+2*b)/3) +
            F(b)
        )

    eps = 0.01
    Iold = np.inf
    I = f38(a, b)
    N = 2
    k = 0

    while abs(I-Iold)/abs(I) > eps:
        k += 1
        N = N*2
        S = np.linspace(a, b, N)
        h = S[1]-S[0]
        Iold = I
        I = np.sum([f38(ai, ai+h) for ai in S[:-1]])

    return [I, k]


n = 5

A = np.zeros([n, n], dtype=np.float32)

for j in range(1, n-1):
    A[j][j] = -(3+sin(j+1)**2*cos(j+1)**5/(j+1+1))

for j in range(1, n-1):
    A[j][j-1] = 1
    A[j][j+1] = (1+cos(j+1)**2)

A[0][0] = 1
A[n-1][n-1] = 1
A[n-1][n-2] = -0.9

b = np.zeros(n, dtype=np.float32)

for j in range(1, n-1):
    def F(t):
        return f(j+1, t)
    if n <= 1000:
        b[j] = -Int(j+1)[0]
    else:
        b[j] = -spint.quad(F, 0, 1)[0]
b[n-1] = 1

x = b/np.diag(A)
eps = 0.001
xold = b+1000*eps
E = np.identity(n)

# print('Число обусловленности СЛАУ %s' % np.linalg.cond(A))

WWT = A@A.T
WT = A.T

N = 0
r = 1000

while norm(r) > eps:
    N += 1
    rold = r
    r = A@x-b

    if N % 10 == 0:
        print('Число итераций %s, норма невязки %s' % (N, norm(r)))

    WWTR = WWT@r
    mu = (r@WWTR)/(WWTR@WWTR)

    xold = x
    x = x-(mu*WT)@r

print()
print(f'Число итераций {N}')
print(np.linalg.norm(x))
# print(np.linalg.norm(np.linalg.solve(A,b)))
