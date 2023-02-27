import math


def summation(f, range):
    r = 0
    for i in range:
        r += f(i)
    return r


# Weddle's rule 6-th order
def simpson(f, h, min, max):
    n = math.floor((max - min) / (h * 2))
    print('n', n)
    print('h', h)

    def g(i): return f(min + i * h)

    a = g(0)
    b = summation(lambda i: g(2 * i - 1), range(1, n + 1))
    c = summation(lambda i: g(2 * i), range(1, n))
    d = g(2 * n)

    return (h / 3) * (a + (4 * b) + (2 * c) + d)


def f(x): return x


# h = (x-x0)/n
#
result = simpson(f, 1/5, 0, 1)
print(result)
