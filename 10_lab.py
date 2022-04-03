import math


def MPD(a, b, eps=1e-5):
    """Метод Дихотомии"""

    def f(x, eps=1e-5):
        if x == 0:
            x = eps
        return math.sqrt(x+1)-1/x

    n = 0
    while abs(b - a) > eps:
        n += 1
        x = (a + b) / 2.0
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x

    print(f'X = {x}')


def newton(epsilon, max_iter):
    """Метод Ньютона"""

    def f(x): return x**3 - x**2 - 1
    def Df(x): return 3*x**2 - 2*x

    xn = 1
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print(f'Решение найдено после {n} итераций.')
            print(f'X = {xn}')
            return None

        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Нулевая производная. Решение не найдено.')
            return None
        xn = xn - fxn/Dfxn
    print('Сделано максимальное количество итераций и решение не найдено')


if __name__ == '__main__':
    MPD(0, 1)
    # newton(1e-10, 10)
